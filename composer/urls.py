from django.urls import path
from . import views

urlpatterns = [
    # Modify name inside the quotation marks to change the URL path
    path("", views.index, name = "composerindex"), # HOMEPAGE
    path("about/", views.about, name = "composerabout"),
]