class Personel():
       def __init__(self , id, ad ,soyad , cins , cadde, ilce, sehir ):
              self.id = id
              self.ad = ad
              self.soyad = soyad
              self.cins = cins
              self.cadde = cadde,
              self.ilce = ilce
              self.sehir = sehir
       def adresyaz(self):
              if self.cins == "E":
                     bas = "Sn. Bay"
              else:
                     bas = "Sn Bayan"
              print(""" 
              {}- {} {}
              {}
              {}-{}
              """.format(bas, self.ad, self.soyad ,self.cadde, self.ilce,self.sehir))
personel = Personel(id = 1, ad ="Şamil" , soyad ="Yılmaz" , cins= "E" ,
  ilce = "Kadıköy" , cadde="Atatürk Cad" , sehir ="Istanbul")
personel.adresyaz()
print(personel.cadde)
       
     
