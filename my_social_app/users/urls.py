from django.urls import path
from .views import register, login_view, logout_view, home, profile, edit_profile, home1, delete_profile
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('users/register/', register, name='register'),
    path('users/login/', login_view, name='login'),
    path('users/logout/', logout_view, name='logout'),
    path("users/home/", home, name="home"),  # Home page URL
    path('users/profile/', profile, name='profile'),
    path('users/profile/edit/', edit_profile, name='edit_profile'),
    path('users/password_reset/', auth_views.PasswordResetView.as_view(template_name="users/password_reset.html"),
         name='password_reset'),
    path('users/password_reset_done/',
         auth_views.PasswordResetDoneView.as_view(template_name="users/password_reset_done.html"),
         name='password_reset_done'),
    path('users/reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name="users/password_reset_confirm.html"),
         name='password_reset_confirm'),
    path('users/reset/done/',
         auth_views.PasswordResetCompleteView.as_view(template_name="users/password_reset_complete.html"),
         name='password_reset_complete'),

    # Change password (for logged-in users)
    path('users/password_change/', auth_views.PasswordChangeView.as_view(template_name="users/password_change.html"),
         name='password_change'),
    path('users/password_change_done/',
         auth_views.PasswordChangeDoneView.as_view(template_name="users/password_change_done.html"),
         name='password_change_done'),
    path('', home1, name='home1'),
    path('delete-profile/', delete_profile, name='delete_profile'),
]
