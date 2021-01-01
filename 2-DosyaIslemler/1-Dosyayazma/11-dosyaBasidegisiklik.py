with open("dosya2.txt","r+",encoding = "utf-8") as dosya:
    icerik = dosya.read()
    icerik = "Yeni Selen Yılmaz-Dosya Başı\n"+ icerik
    dosya.seek(0)
    dosya.write(icerik)
    