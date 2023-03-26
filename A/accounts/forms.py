from django import forms


class UserRegisterForm(forms.Form):
    username = forms.CharField(label="Username")
    email = forms.EmailField(label="Email")
    password = forms.CharField()


class UserLoginForm(forms.Form):
    username = forms.CharField(label="Username")
    password = forms.CharField()
