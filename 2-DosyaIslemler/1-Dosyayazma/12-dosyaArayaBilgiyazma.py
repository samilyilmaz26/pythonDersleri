with open("dosya2.txt","r+",encoding = "utf-8") as dosya:
    liste = dosya.readlines()
    liste.insert(2,"Araya Bilgi Yazma\n")
    dosya.seek(0)
    for i in liste:
        dosya.write(i)
    dosya.seek(0)
    print(dosya.read())