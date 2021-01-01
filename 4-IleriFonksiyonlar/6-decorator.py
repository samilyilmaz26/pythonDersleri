user = "Şamil"
password = "123"

def sayfa1(user,password):
    if user == "Şamil" and password == "123":
        print ("login Başarılı")
        print("Sayafamıza Hoşgeldiniz")
    else:
        print ("Bu Sayfaya Giriş Yetkiniz Yok")
def sayfa2(user,password):
    if user == "Şamil" and password == "123":
        print ("login Başarılı")
        print("Sayafamıza Hoşgeldiniz")
    else:
        print ("Bu Sayfaya Giriş Yetkiniz Yok")
    


def login(fonksiyon):
    print("Merhaba")
    def wrapper(user,password):
         if user == "Şamil" and password == "123":
             print ("login Başarılı")
             print("Sayafamıza Hoşgeldiniz")
         else:
            print("Bu Sayfaya Giriş Yetkiniz Yok")
    return wrapper
 
@login
def sayfa3(user, password):
     pass
sayfa3("Şamil","123")
    
        