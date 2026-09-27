from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.index, name="index"),
    path("post/<str:slug>", views.detail, name="detail"),
    path("about", views.about_view, name="about"),
    path("contact", views.contact_view, name="contact"),
    path("new_something_url", views.new_url_view, name="new_page_url"),
    path("old_something_url", views.old_url_redirect, name="old_page_url"),
]