from django.urls import path, include
from accounts import views

# APP NAME
app_name = 'accounts'

urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signup'),
]