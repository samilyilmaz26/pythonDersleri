dosya = open("dosya2.txt" ,"r" , encoding="utf-8")
bilgiler = dosya.readline() #bir satır okur
print(bilgiler)
dosya.close()