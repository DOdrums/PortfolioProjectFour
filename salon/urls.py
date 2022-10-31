from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.HomePage.as_view(), name="home"),
    path('book', views.BookingModule.as_view(), name="book"),
    path('thankyou', views.ThankYou.as_view(), name="thankyou"),
    path('book-error', views.BookError.as_view(), name="book-error"),
]