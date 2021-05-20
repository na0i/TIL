from django.contrib.auth import get_user_model
from django.db import models
from django.db.models import fields
from rest_framework import serializers

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'nickname',)