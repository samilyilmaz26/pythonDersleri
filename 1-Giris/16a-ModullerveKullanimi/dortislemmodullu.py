from dortislemModule import cikar,carp,bol,topla
from os import system    

def cevir(metin):
    return float(input(metin))


while True:
    system('cls')
    iskod = input("İşlem Kodu :")
    s1 = cevir("Birinci Sayi")
    s2 = cevir("İkinci Sayi")
    if iskod == "+":
        sonuc = topla(s1,s2)
    elif iskod == "-":
        sonuc = cikar(s1,s2)
    elif iskod == "*":
        sonuc = carp(s1,s2)
    elif iskod == "/":
        sonuc = bol(s1,s2)
    else:
        print("Yanlış İşlem Kodu ")
        break
    print( "Sonuç :" +str(sonuc))
    print(input("devam için herhengi bir tuşa basın"))

