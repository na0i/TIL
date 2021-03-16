from django import forms
from .models import Article

class ContactForm(forms.Form):
    name = forms.CharField(min_length=2, max_length=5)
    email = forms.EmailField()
    age = forms.IntegerField(min_value=3, max_value=100)
    content = forms.CharField(widget=forms.Textarea)

class ArticleForm(forms.ModelForm):
    # 장고에서 쓰는 예약어
    class Meta:
        model = Article
        fields = '__all__'