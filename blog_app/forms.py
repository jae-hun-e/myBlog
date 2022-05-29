from django import forms
from .models import Blog


class BlogFrom(forms.Form):
    # 내가 입력받고자 하는 값을
    title = forms.CharField()
    body = forms.CharField(widget=forms.Textarea)


class BlogModelForm(forms.ModelForm):
    class Meta:
        model = Blog  # models 안에서 받아옴
        fields = '__all__'  # blog객체 안에 있는 모든Fields
        # fields = ['title', 'body']  # blog 객체 안에 있는 특정 fileds

