def fakt (sayi):
    faktoryel = 1
    if sayi == 1 or sayi == 0:
        return faktoryel
    else:
        while (sayi>=1):
            faktoryel *= sayi
            sayi -= 1
        return faktoryel
s = float(input("Sayı ")) 
hesap = fakt(s)*fakt(s-1)/fakt(s+1)
print(str(hesap))     
        
