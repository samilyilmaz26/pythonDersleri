#https://myaccount.google.com/lesssecureapps
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import sys

mesaj = MIMEMultipart() 
mesaj["From"] = input("Kimden  :")
mesaj["To"]  = input("Kime :")
mesaj["Subject"] = input("Konu  :")
yazi = input("mail içerik  :")
user = input("user name  :")
password = input("Password   :")
mesaj_govdesi =  MIMEText(yazi,"plain")
mesaj.attach(mesaj_govdesi)


try:
    mail =  smtplib.SMTP("smtp.gmail.com",587) # bağlantı
    mail.ehlo() # stmp tanıtım
    mail.starttls() # kullanıcı adı ve şifre
    mail.login(user,password)
    mail.sendmail(mesaj["From"],mesaj["To"],mesaj.as_string())  # mail gönderme
    print("Mail başarıyla gönderildi....")
    mail.close()
except:
    sys.stderr.write("Mail gönderilemedi ...") # Herhangi bir bağlanma sorunu veya mail gönderme sorunu olursa
    sys.stderr.flush()