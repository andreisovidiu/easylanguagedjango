from django.urls import path
from . import views

urlpatterns = [
    # Modify name inside the quotation marks to change the URL path
    path("register/", views.register, name = "studentsregister"),
    path("login/", views.login, name = "studentslogin"),
]   


