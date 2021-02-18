class Temel():
    def __init__(self, ad, soyad ,cadde ,ilce,sehir):
        self.ad = ad
        self.soyad = soyad
        self.ilce = ilce
        self.sehir = sehir
        self.cadde = cadde
    def adresal(self):
        adresList = []
        adresList.append(self.fullname())
        adresList.append(self.cadde)
        adresList.append(self.ilce + "-"+ self.sehir)
        return adresList
    def fullname(self):
        return self.ad + " " + self.soyad

class Ogrenci(Temel):
    pass

class Egitmen(Temel):
    def __init__(self, ad, soyad ,cadde ,ilce,sehir,maas,unvan):
        super().__init__(ad, soyad ,cadde ,ilce,sehir)
        self.maas = maas
        self.unvan = unvan
    def fullname(self):
        return self.unvan + self.ad + " " + self.soyad
    def maasal(self):
        return self.maas
    
 