from django import forms

class RegisterForm(forms.Form):
    username = forms.CharField(label="Kullanıcı Adı" ,min_length=3 )
    password = forms.CharField(label = "Şifre " ,widget = forms.PasswordInput )
    confirm =  forms.CharField(label = "Şifre Tekrar" ,widget = forms.PasswordInput  )
    def clean(self):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        confirm = self.cleaned_data.get("confirm")
        if password and username and password != confirm:
            raise forms.ValidationError("Şifreler Uyumsuz")
        values = {
        "username": username,
        "password": password
        }
        return values
class LoginForm(forms.Form):
    username = forms.CharField(label="Kullanıcı Adı")
    password = forms.CharField(label = "Şifre " ,widget = forms.PasswordInput  )
class PesonelForm(forms.Form):
    name = forms.CharField(label="Personel Adı")
    surname = forms.CharField(label="Personel Soyadı")
    salary = forms.CharField(label="Maaşı") 
    birthdate = forms.DateField(label="Doğum Tarihi")