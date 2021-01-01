from datetime import datetime
tarih = datetime.today()
print (tarih)
print(tarih.year)
print(tarih.month)
print(tarih.time)
print(tarih.hour)
print("----------ctime-------------")
 
print(tarih.ctime())
# strftime() fonksiyonu
#     Yıl bilgisini almak için : %Y
#     Ay ismini almak için : %B
#     Gün ismini almak için : %A
#     Saat bilgisini almak için : %X
#     Gün bilgisini almak için : %D
print(datetime.strftime(tarih,"%Y"))

print(datetime.strftime(tarih,"%B"))
print("----------------Fark-------------------")
tarih = datetime(2019,11,1) 
bugun = datetime.now()
fark = bugun-tarih
print(fark)