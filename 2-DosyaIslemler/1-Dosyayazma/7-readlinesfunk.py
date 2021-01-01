dosya = open("dosya2.txt" ,"r" , encoding="utf-8")
bilgiler = dosya.readlines() # satırlar liste şeklinde döner
print(bilgiler)
dosya.close()