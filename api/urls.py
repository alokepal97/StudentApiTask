from api.views import StudentViewSet
from rest_framework import routers
from django.urls import path, include
from .views import CustomAuthToken


router = routers.DefaultRouter()
router.register(r'student', StudentViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('authenticate/', CustomAuthToken.as_view())
]
