from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.HomePage.as_view(), name="home"),
    path('book', views.BookingModule.as_view(), name="book")
]