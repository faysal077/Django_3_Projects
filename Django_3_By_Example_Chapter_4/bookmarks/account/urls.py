
from django.contrib.auth import views as auth_views
from django.urls import path,include,re_path
from . import views
from .views import dashboard
urlpatterns = [
    #path('login/', views.user_Login, name='login'),
    # Log-in and Logout
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('',dashboard,name='dashboard'),
    # change password urls
    path('password_change/',auth_views.PasswordChangeView.as_view(),name='password_change'),
    path('password_change/done/',auth_views.PasswordChangeDoneView.as_view(),name='password_change_done'),
    # reset password urls
    path('password_reset/',
         auth_views.PasswordResetView.as_view(template_name="registration/password_reset_form.html"),
         name='password_reset'),
    path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name="registration/password_change_form.html"), name='password_reset_confirm'),
    path('reset/done/',auth_views.PasswordResetCompleteView.as_view(template_name="registration/password_reset_done.html"),name='password_reset_complete'),
    #path('reset/Mw/acmlxi[A-Z a-z 0-9]*/',auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complete'),
]
