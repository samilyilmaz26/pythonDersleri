dosya = open("dosya2.txt" ,"r" , encoding="utf-8")
#dosyaz = open("dosyaz.txt" ,"r" , encoding="utf-8")
 
for j in dosya:
    print(j , end ="")
dosya.close()
    