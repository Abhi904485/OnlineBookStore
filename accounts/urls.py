from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.urls import include

from .views import (login_page, register_page, logout_page, profile, activate, account_activation_sent)

app_name = 'account'
urlpatterns = [
        url(r'^login/$', login_page, name='login'),
        url(r'^logout/$', logout_page, name='logout'),
        url(r'^register/$', register_page, name='register'),
        url(r'^profile/', profile, name="profile"),
        # url(r'^reset/$',
        #     auth_views.PasswordResetView.as_view(
        #             template_name='password_reset.html',
        #             email_template_name='password_reset_email.html',
        #             subject_template_name='password_reset_subject.txt'
        #     ),
        #     name='password_reset'),
        # url(r'^reset/done/$',
        #     auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'),
        #     name='password_reset_done'),
        # url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        #     auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'),
        #     name='password_reset_confirm'),
        # url(r'^reset/complete/$',
        #     auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),
        #     name='password_reset_complete'),
        # url(r'^account_activation_sent/$', account_activation_sent, name='account_activation_sent'),
        # url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        #     activate, name='activate'),
        # url(r'^settings/password/$', auth_views.PasswordChangeView.as_view(template_name='accounts/password_change.html'),
        #     name='password_change'),
        # url(r'^settings/password/done/$',
        #     auth_views.PasswordChangeDoneView.as_view(template_name='password_change_done.html'),
        #     name='password_change_done'),
]
