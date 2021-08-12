from django.urls import path
from .views import LoginView, CreateAuthorView, CreateUserView, LogoutView
urlpatterns = [
    path('login/', LoginView, name="login"),
    path('author/', CreateAuthorView, name='create-author'),
    path('viewer/', CreateUserView, name='create-user'),
    path('logout/', LogoutView, name='logout'),
]
