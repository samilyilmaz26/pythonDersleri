from wtforms import Form, StringField, TextAreaField, PasswordField,BooleanField, validators

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
class ArticleForm(Form):
    title = StringField('Başlık', [validators.Length(min=4, max=50)])
    content  = TextAreaField('içerik', [validators.Length(min=10, max=200)])
    
