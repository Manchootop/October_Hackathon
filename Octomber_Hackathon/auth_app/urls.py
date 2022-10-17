from django.urls import path

from Octomber_Hackathon.auth_app.views import RegisterView, LoginView

urlpatterns = (
    path('register/', RegisterView.as_view(), name='register user'),
    path('login/', LoginView.as_view(), name='login user'),
)
