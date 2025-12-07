from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
"CommentForm(forms.ModelForm)", "model = Comment", "content"
"TagWidget()", "tags", "widgets"
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email']


