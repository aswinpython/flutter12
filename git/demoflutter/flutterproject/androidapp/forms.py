from django import forms
from .models import Android
class AndroidForm(forms.ModelForm):
    class Meta:
        model=Android
        fields=['name','desc','year','img']

