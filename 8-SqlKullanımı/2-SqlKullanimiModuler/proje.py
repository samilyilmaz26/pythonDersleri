from sqlModule import Listele,Ekle,Guncel,Sil

print("""******************************************
1-Listele
2- Ekle 
3- Guncelle
4- Sil
9- çıkış
**********************************************""")

while True:
    secim = int(input("Seçim   :")) 
    if secim == 1:
        Listele()
    elif secim == 2:
        ad = input("İsim  :")
        soyad = input("Soyad  :")
        maas  = input("Maas  :")
        Ekle(ad,soyad,maas)
    elif secim == 3:
        id = input("İd  :")
        maas  = input("Maas  :")
        Guncel(id ,maas)
    elif secim == 4:
        id = input("İd  :")
        Sil(id)
    
    elif secim == 9:
        break
    else:
        print("Yanlış Seçim")
    
       