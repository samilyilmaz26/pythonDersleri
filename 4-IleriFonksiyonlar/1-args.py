def f1(*args): # İstediğimiz sayıda argüman gönderebiliyoruz.
    for i in args:
        print(i)
f1("Elma","Armut ","Portakal")
def f2(baslik,*args): 
    print(baslik)
    for i in args:
        print(i)
f2("Meyvalar" ,"Elma","Armut ","Portakal")