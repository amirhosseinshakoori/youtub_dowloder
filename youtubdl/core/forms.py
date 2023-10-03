from django import forms
from . models import SaveUrloath

class SaveUrloathform(forms.ModelForm):
    class Meta:
        model = SaveUrloath
        fields = {'link'}