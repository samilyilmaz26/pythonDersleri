from datetime import date
class Personel():
   
    def __init__(self , id, ad ,soyad  ):
        self.id = id
        self.ad = ad
        self.soyad = soyad
personel = Personel( id = 1, ad= "Şamil",soyad="Yılmaz"  )  
print(personel.ad + personel.soyad)
personel2 = Personel( id = 2, ad= "Selen",soyad="Yılmaz") 
print(personel2.ad + personel2.soyad) 