from django.urls import path
from . import views
# . implies current directory where urls.py is located

urlpatterns = [
    path("", views.index, name="index"),
    path("name1", views.name1, name="name1"),
    path("name2", views.name2, name="name2"),
    path("<str:name>", views.greet, name="greet")
]