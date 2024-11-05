from django.urls import path
from . import views


urlpatterns=[
    path("", views.home, name="home"),
    path("add-todo/", views.addTodo, name="add-todo"),
    path("delete-todo/<int:pk>/", views.deleteTodo, name="delete-todo"),
    path('toggle-todo/<int:todo_id>/', views.toggle_todo, name='toggle-todo'),



    path("accounts/login/", views.loginUser, name="login"),
    path("accounts/signup/", views.signupUser, name="signup"),
    path("accounts/logout/", views.logoutUser, name="logout"),
]