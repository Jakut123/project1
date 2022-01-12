from django.contrib import admin
from django.contrib.auth import get_user_model
from django.urls import path, include

User = get_user_model()

admin.site.register(User)



