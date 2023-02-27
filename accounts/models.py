from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


class CustomUser(AbstractUser):
    """Custom user model."""

    name = models.CharField(_("Full Name"), max_length=100, null=True, blank=True)

    def __str__(self):
        return self.username
