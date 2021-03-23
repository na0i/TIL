from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

class CustomUserCreationForm(UserCreationForm):
    # little customize
    class Meta:
        # get_user_model은 클래스 반환 함수
        model = get_user_model()
        fields = ('username', )