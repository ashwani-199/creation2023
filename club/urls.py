from django.urls import path
from . import views

urlpatterns = [
    path("", views.PostList.as_view(), name="home"),
    path("about", views.about, name="about"),
    path("<slug:slug>/", views.post_detail, name="post_detail"),
    path("contact", views.contact, name="contact"),
]
