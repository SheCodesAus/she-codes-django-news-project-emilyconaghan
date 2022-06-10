from django.urls import path
from .views import CreateAccountView, UserInterfaceView

app_name = 'users'

urlpatterns = [
    path('create-account/', CreateAccountView.as_view(),
         name='createAccount'),
    path('user-interface/', UserInterfaceView.as_view(), name='userInterface'),
]
