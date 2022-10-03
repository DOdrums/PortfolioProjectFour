from . import views
from django.urls import path

urlpatterns = [
    path('', views.HomePage.as_view(), name="treatments-list"),
    path('book', views.BookingModule.as_view(), name="book")
]