from django import forms
from . import UserField

class UserFieldForm(forms.ModelForm):
    class Meta:
        model = UserField
        fields = "__all__"
