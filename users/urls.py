from django.urls import path
from .views import sign_up


urlpatterns = [
    path('', sign_up, name='register')
]
