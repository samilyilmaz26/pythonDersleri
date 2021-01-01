from datetime import date
class Personel():
   
    def __init__(self , id, ad ,soyad , maas , sirketkod  ,mail =" " ,kayit_tarih = date.today()):
        self.id = id
        self.ad = ad
        self.soyad = soyad
        self.maas = maas
        self.sirketkod = sirketkod
        if self.sirketkod ==1:
            self.mail = self.ad + '@' + 'abc.com'
        else:
            self.mail = self.ad + '@' + 'xyz.com'
        self.kayit_tarih = kayit_tarih
personel = Personel( id = 1, ad= "Şamil",soyad="Yılmaz" ,maas = 3000 ,sirketkod = 1 )  
print(personel.kayit_tarih)
print(personel.mail)
personel2 = Personel( id = 2, ad= "Selen",soyad="Yılmaz" ,maas = 3000 ,sirketkod = 2) 
print(personel2.kayit_tarih)
print(personel2.mail)