from datetime import date
class Personel():
    id = 1
    ad = "Şamil"
    soyad ="Yılmaz"
    maas = 2500
    sirketkod = 1
    mail = ""
    kayit_tarih = date.today()
    def __init__(self):
        if self.sirketkod == 1:
            self.mail = self.ad+ "@" + "abc.com"   
        else:
            self.mail = self.ad + "@" + "xyz.com"
    
personel = Personel()
print(personel.mail)

