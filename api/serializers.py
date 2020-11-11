from django.contrib.auth.models import User
from api.models import Student
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

class StudentSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    first_name = serializers.CharField(
        source='user.first_name', required=True)
    last_name = serializers.CharField(source='user.last_name')
    username = serializers.CharField(source='user.username', read_only=True)
    email = serializers.CharField(source='user.email', required=True)
    password = serializers.CharField(source = 'user.password')
    is_active = serializers.CharField(source='user.is_active', read_only=True)

    class Meta:
        model = Student
        fields = ['id', 'first_name', 'last_name', 'phone', 'username', 'email', 'password',
                  'is_active']

    def validate_email(self, email):
        userObj = User.objects.filter(email=email)
        if (userObj.count() > 0):
            raise serializers.ValidationError(
                "Already exist")
        return email
