def topla(a,b):
    return a+b 
def cikar(a,b):
    return a-b 
def  carp(a,b):
    return a*b 
def bol(a,b):
    try:
        return a/b 
    except ZeroDivisionError:  
        print("Sayı Sıfıra Bölünemez")
def cevir(metin):
    try:
        return float(input(metin))
    except ValueError:
        print("Numerik sayı girilmedi")
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

print( "Sonuç :" +str(sonuc))
