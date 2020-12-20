from django.urls import path, include
from accounts import views

# APP NAME
app_name = 'accounts'

urlpatterns = [
    path('sigin/', views.Sigin.as_view(), name='sigin'),
]