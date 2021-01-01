from django import forms
from . models import Cities,Personel
class CitiesForm(forms.ModelForm):
    class Meta():
        model = Cities
        fields = ["name","description"]
class PersonelForm(forms.ModelForm):
    class Meta():
        model = Personel
        fields = ["name","surname","salary","birthdate" ,"cityid"]
        widgets = {'birthdate': forms.HiddenInput()}
        