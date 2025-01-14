from django.urls import path, re_path
from django.views.static import serve

from .views import index, healthcheck, example500, deploy, logout, LoginView, artists, venues, privacy, terms, contact_us, ConfirmEmailView

urlpatterns = [
    path('', index, name="home"),
    path('deploy', deploy, name="deploy"),
    path('artists/', artists, name="artists"),
    path('venues/', venues, name="venues"),
    path('contact-us/', contact_us, name="contact_us"),
    path('privacy/', privacy, name="privacy"),
    path('privacy-2/', privacy, name="privacy"),
    path('terms/', terms, name="terms"),
    path('healthcheck', healthcheck),
    path('example500', example500),
    path('account/log_out/', logout, name="opus_logout"),
    path('account/login/', LoginView.as_view(), name="opus_login"),
    re_path(r"^account/confirm_email/(?P<key>\w+)/$", ConfirmEmailView.as_view(), name="opus_confirm_email"),
    re_path(r'^favicon.ico$', serve, {
        'document_root': '/app/static/images/favicon.ico',
        'path': '.'
    }),
]
