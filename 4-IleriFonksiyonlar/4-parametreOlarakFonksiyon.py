def toplama(a,b):
    return a + b
def cikarma(a,b):
    return a-b
def carpma(a,b):
    return a * b
def bolme(a,b):
    return a / b
def dortislem(f1,f2,f3,f4,iskod): # Tanımladığımız 4 fonksiyonu da argüman  .
    if (iskod == "+"):
        print(f1(3,4))
    elif (iskod == "-"):
        print(f2(3,4))
    elif (iskod == "*"):
        print(f3(3,4))
    elif (iskod== "/"):
        print(iskod(3,4))
    else:
        print("Geçersiz işlem adı...")
print(dortislem(toplama,cikarma,carpma,bolme ,"*"))
