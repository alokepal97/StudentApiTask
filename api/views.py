from api.token_expire_handler import expires_in, token_expire_handler
from django.contrib.auth.models import User, UserManager
import rest_framework
from api.serializers import StudentSerializer, serializers
from api.models import Student
from django.shortcuts import get_object_or_404, render
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
# Create your views here.
# ViewSets define the view behavior.
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.contrib.auth.models import Group, User
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny


class ActionBasedPermission(AllowAny):
    """
    Grant or deny access to a view, based on a mapping in view.action_permissions
    """

    def has_permission(self, request, view):
        for klass, actions in getattr(view, 'action_permissions', {}).items():
            if view.action in actions:
                return klass().has_permission(request, view)
        return False


# Students crud
class StudentViewSet(viewsets.ModelViewSet):

    def create(self, request):
        s = StudentSerializer(data=request.data)
        if s.is_valid():
            user = User.objects.create_user(first_name=request.data['first_name'],
                                            last_name=request.data['last_name'],
                                            username=request.data['email'],
                                            email=request.data['email'],
                                            password=request.data['password'])
            if user is not None:
                student = Student.objects.create(user=user,
                                                   phone=request.data['phone'])
                serializer_class = StudentSerializer(student)
                return Response(serializer_class.data, status=status.HTTP_200_OK)
        else:
            return Response(s.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):

        student = get_object_or_404(Student, pk=pk)

        std = Student.objects.get(id=pk)
        std.phone = request.data.get('phone', std.phone)
        std.save()

        user = User.objects.get(pk=std.user.id)
        user.first_name = request.data.get('first_name', user.first_name)
        user.last_name = request.data.get('last_name', user.last_name)
        user.email = request.data.get('email', user.email)
        user.save()
        serializer_class = StudentSerializer(Student.objects.get(id=pk))
        return Response(serializer_class.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        student = get_object_or_404(Student.objects.all(), pk=pk)

        if student.user != request.user:
            return Response({'response': 'You dont have permission to edit that.'})

        queryset = get_object_or_404(Student.objects.all(), pk=pk)
        serializer_class = StudentSerializer(queryset)
        headers = self.get_success_headers(serializer_class.data)
        return Response(serializer_class.data, status=status.HTTP_200_OK, headers=headers)

    def destroy(self, request, pk=None):
        student = get_object_or_404(Student.objects.all(), pk=pk)
        if student.user != request.user:
            return Response({'response': 'You dont have permission to delete that.'})
        student.delete()
        user=User.objects.get(id=student.user.id)
        user.delete()
        content = {'details': 'Not found.'}
        return Response(content, status=status.HTTP_200_OK)


    queryset = Student.objects.all().prefetch_related('user')
    serializer_class = StudentSerializer
    permission_classes = (ActionBasedPermission,)

    action_permissions = {
        IsAuthenticated: ['update', 'partial_update', 'destroy', 'list', 'retrieve'],
        AllowAny: ['create']
    }

@permission_classes((AllowAny,))
class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)

        is_expired, token = token_expire_handler(token)

        return Response({
            'token': token.key,
            'expires_in': expires_in(token),
            'user_id': user.pk,
            'email': user.email
        })
