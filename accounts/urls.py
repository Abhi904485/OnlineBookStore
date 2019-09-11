from django.conf.urls import url
from django.contrib.auth import views as auth_view
from .views import (login_page, register_page, logout_page, profile, )

app_name = 'account'
urlpatterns = [
        url(r'^login/$', login_page, name='login'),
        url(r'^logout/$', logout_page, name='logout'),
        url(r'^register/$', register_page, name='register'),
        url('^profile/', profile, name="profile"),
        url('^password-reset/', auth_view.PasswordResetView.as_view(template_name="password_reset.html"),
            name="password_reset"),

        url('^password-reset-confirm/<uidb64>/<token>/',
            auth_view.PasswordResetConfirmView.as_view(template_name="password_reset_confirm.html"),
            name="password_reset_confirm"),

        url('^password-reset/done/', auth_view.PasswordResetDoneView.as_view(template_name="password_reset_done.html"),
            name="password_reset_done"),
        url('^password-reset-complete/',
            auth_view.PasswordResetCompleteView.as_view(template_name="password_reset_complete.html"),
            name="password_reset_complete"),
]
