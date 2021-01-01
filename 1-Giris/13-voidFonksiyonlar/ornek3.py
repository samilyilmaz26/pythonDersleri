def faktoryel(sayi):
    faktoryel =1
    if sayi == 0 or sayi == 1:
        print(faktoryel)
    else:
        while (sayi >=1):
            faktoryel *= sayi
            sayi -= 1
        print(faktoryel)
        
s = int(input("Sayi : "))
faktoryel(s)
