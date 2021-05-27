from django.contrib.auth import get_user_model
from django.db import models
from django.db.models import fields
from rest_framework import serializers
#
User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username',)

from rest_framework import serializers

from allauth.account.adapter import get_adapter
from allauth.account.utils import setup_user_email

from rest_auth.registration.serializers import RegisterSerializer
try:
    from movies.serializers import GenreSerializer
except ImportError:
    import sys
    GenreSerializer = sys.modules[__package__ + '.GenreSerializer']


class CustomRegisterSerializer(RegisterSerializer):
    nickname = serializers.CharField(required=True, max_length=10)
    date_of_birth = models.DateTimeField(blank=True, null=True)
    like_genres = GenreSerializer(many=True)

    def get_cleaned_data(self):
        data_dict = super().get_cleaned_data()
        data_dict['nickname'] = self.validated_data.get('nickname', '')
        data_dict['date_of_birth'] = self.validated_data.get('date_of_birth', '')
        data_dict['like_genres'] = self.validated_data.get('like_genres', '')
        return data_dict

