from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>", views.entry, name="entry"),
    path("search", views.search, name="search"),
    path("<str:title>", views.md_entry, name="md_entry"),
    path("new_page", views.new_page, name="new_page")
]
