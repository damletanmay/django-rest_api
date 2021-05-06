from django.urls import path
from . import views

urlpatterns = [
    path('admin/advisor/',views.addAdvisor), # for adding Advisors
    path('user/register/',views.registerUser), # for user register / account making
    path('user/login/',views.loginUser), # for user login
    path('user/<int:user_id>/advisor/',views.viewAdvisor), # for getting all advisors
    path('user/<int:user_id>/advisor/<int:advisor_id>/',views.bookACall), # for booking a call
    path('user/<int:user_id>/advisor/booking/',views.viewBookings), # for viewing all bookings of a user.
]
