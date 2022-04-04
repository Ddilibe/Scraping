from django.forms import forms
from .models import Comment


class NewsCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("name", "email", "content")
        widgets = {
            "name": forms.TextInput(attrs={"class":"col-sm-12"})
            "email": forms.TextInput(attrs={"class":"col-sm-12"})
            "content": forms.TextInput(attrs={"class":"form_control"})
        }