isim = "şamil"
print(isim.upper())
isim = "ŞAMİL"
print(isim.lower())
str = "Gurultu"
print(str.replace ("u" ,"ü"))
print(isim.startswith("Ş"))
print(isim.startswith("ş"))
print(isim.endswith("L"))
str  = "..........................Şamil.........................."
str = str.strip(".")
print(str)
print("      Şamil".lstrip(" "))
print("Şamil       ".rstrip(" "))
liste = ["01","01","2020"]
print("/".join(liste))
print("Şamil Yılmazavcı".count("a"))
print("Şamil Yılmazavcı".count(" "))
print("Şamil Yılmazavcı".count("a",2))
print("gürültü".find("ü"))
print("gürültü".find("u"))
print("gürültü".rfind("ü"))