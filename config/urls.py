from django.contrib import admin
from django.urls import path, include
from dj_rest_auth.registration.views import VerifyEmailView, ConfirmEmailView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/dj-rest-auth/', include('dj_rest_auth.urls')),
    path(
        'api/v1/dj-rest-auth/registration/account-confirm-email/<str:key>/',
        ConfirmEmailView.as_view(),
    ),
    # Needs to be defined before the registration path
    path('api/v1/dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')),
    path(
        'api/v1/dj-rest-auth/account-confirm-email/',
        VerifyEmailView.as_view(),
        name='account_email_verification_sent'
    ),
    path("api/v1/", include('posts.urls', namespace="posts")),
    path("api/v1/", include('accounts.urls', namespace="users")),

]
