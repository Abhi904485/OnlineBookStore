from django.conf.urls import url
from django.contrib.auth import views as auth_view
from django.urls import include

from .views import (login_page, register_page, logout_page, profile, activate, account_activation_sent)

app_name = 'account'
urlpatterns = [
        url(r'^login/$', login_page, name='login'),
        url(r'^logout/$', logout_page, name='logout'),
        url(r'^register/$', register_page, name='register'),
        url(r'^profile/', profile, name="profile"),
        url(r'^password-reset/', auth_view.PasswordResetView.as_view(template_name="password_reset.html"),
            name="password_reset"),
        url(r'^password-reset-confirm/<uidb64>/<token>/',
            auth_view.PasswordResetConfirmView.as_view(template_name="password_reset_confirm.html"),
            name="password_reset_confirm"),
        url(r'^password-reset/done/', auth_view.PasswordResetDoneView.as_view(template_name="password_reset_done.html"),
            name="password_reset_done"),
        url(r'^password-reset-complete/',
            auth_view.PasswordResetCompleteView.as_view(template_name="password_reset_complete.html"),
            name="password_reset_complete"),
        url(r'^account_activation_sent/$', account_activation_sent, name='account_activation_sent'),
        url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
            activate, name='activate'),
]
