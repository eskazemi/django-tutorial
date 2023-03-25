from django import forms
from .models import Todo


class TodoCreateForm(forms.Form):
    title = forms.CharField(label="Title")
    body = forms.CharField(label="Content", required=False)


class TodoUpdateForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ["title", "body"]

