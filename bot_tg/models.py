from django.db import models 
from django.contrib.auth import get_user_model
from django.utils import timezone
from datetime import timedelta

User = get_user_model()

class CustomUser(User):
    is_logged_in = models.BooleanField(default=False)

