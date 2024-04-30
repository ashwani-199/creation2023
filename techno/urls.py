from django.urls import path

from .views import ResultView, UploadView
from . import views

app_name = "techno"

urlpatterns = [
    path("", UploadView.as_view(), name="index"),
    path("result/<slug:slug>/", ResultView.as_view(), name="result"),
    path("resize", views.resizeimage, name='resize'),
    path('remove-bg', views.remove_bg),
]