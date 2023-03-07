from django.contrib import admin
from django.urls import path, include, re_path
from dj_rest_auth.registration.views import VerifyEmailView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/", include("posts.urls", namespace='posts')),
    path("api-auth/", include("rest_framework.urls")),
    path("api/v1/dj-rest-auth/", include("dj_rest_auth.urls")),
    path(
        'api/v1/dj-rest-auth/account-confirm-email/<str:key>',
        VerifyEmailView.as_view(template_name=""),
        name='account_email_verification_sent'
    ),
    path("api/v1/dj-rest-auth/registration/", include("dj_rest_auth.registration.urls")),
]
