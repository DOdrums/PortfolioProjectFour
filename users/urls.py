from . import views
from django.urls import path, include

urlpatterns = [
    path('dashboard', views.Dashboard.as_view(), name="dashboard"),
]