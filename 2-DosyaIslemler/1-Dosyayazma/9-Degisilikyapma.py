with open("dosya2.txt","r+",encoding = "utf-8") as dosya:
    dosya.seek(10)
    dosya.write("Selen Yılmaz")
    print(dosya.tell())
    dosya.seek(0)
    bilgi = dosya.readline
    print(bilgi)
    print(dosya.tell())