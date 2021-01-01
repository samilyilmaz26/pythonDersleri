from module import *
import os

print(""""******************************

1 Liste 
2 İsme göre Listele
3 Kayıt Ekleme 
4 İsim  Guncelleme 
5 Kayıt Silme 

e. Çıkış
******************************""")
libs = Libs()
clear = lambda: os.system('cls')
#clear()
while True:
    islem = input("İşlem Kodunu Giriniz")
    if (islem == "1"):
        libs.Liste()
    elif (islem == "2"):
        libs.ListbyName()
    elif (islem == "3"):
        libs.Ekle()
    elif (islem == "4"):
        libs.Guncel()
    elif (islem == "5"):
        libs.Sil()
    elif (islem == "e"):
        break
    else:
        print("Yanlış işlem girildi")
