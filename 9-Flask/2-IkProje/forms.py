from wtforms import Form, StringField, TextAreaField, PasswordField,BooleanField, validators,DecimalField,DateField

class RegisterForm(Form):
    username = StringField('Username', [validators.Length(min=4, max=25)])
    email = StringField('Email Address', [validators.Length(min=6, max=35)])
    password = PasswordField('New Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField('Repeat Password')
    accept_tos = BooleanField('I accept the TOS', [validators.DataRequired()])
class LoginForm(Form):
    username = StringField("Kullanıcı Adı")
    password = PasswordField("Şifreniz")
class CityForm(Form):
    name = StringField('Şehir Ad', [validators.Length(min=4, max=50)])
    description = TextAreaField('Açıklama', [validators.Length(min=4, max=150)])
class PersonelForm(Form):
    name = StringField('Personel Ad', [validators.Length(min=4, max=50)])   
    surname = StringField('Personel Soyad', [validators.Length(min=4, max=50)])
    salary = DecimalField('Maaş',  places=2, rounding=None, use_locale=False, number_format=None)
    