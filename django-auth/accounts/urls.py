from django.urls import path
from accounts import views as account_views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('register/', account_views.Register, name='register'),
    # path('account/', account_views.Account, name='account'),
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='accounts/logout.html'), name='logout'),

    # path('auth/pass/change/',
    #      CustomChangePass.as_view(),
    #      name='change_pass'),
    # path('reset/',
    #      auth_views.PasswordResetView.as_view(
    #          template_name='accounts/auth/password_reset.html'
    #      ),
    #      name='password_reset'),
    # path('reset/confirm/<uidb64>/<token>/',
    #      auth_views.PasswordResetConfirmView.as_view(
    #          template_name='accounts/auth/password_reset_confirm.html'
    #      ),
    #      name='password_reset_confirm'),
    # path('reset/done/',
    #      auth_views.PasswordResetDoneView.as_view(
    #          template_name='accounts/auth/password_reset_done.html'
    #      ),
    #      name='password_reset_done'),
    # path('reset/complete',
    #      auth_views.PasswordResetCompleteView.as_view(
    #          template_name='accounts/auth/password_reset_complete.html'
    #      ),
    #      name='password_reset_complete'),
]