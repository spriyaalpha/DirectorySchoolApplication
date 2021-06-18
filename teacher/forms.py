from django import forms
from .models import PersonalInfoNew

class PersonalInfoForm(forms.ModelForm):
    class Meta:
        model= PersonalInfoNew
        fields = ('File',)
        


