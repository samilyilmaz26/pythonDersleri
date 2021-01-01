def f1(**kwargs):
    print(kwargs)
    
f1(id = 1, ad= "Şamil" ,soyad= "Yılmaz")

def f2(**kwargs):
    for i,j in kwargs.items():
        print("İsim:",i,"Değer:",j)
f2(id = 1, ad= "Şamil" ,soyad= "Yılmaz")