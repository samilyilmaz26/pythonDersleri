#Sözlük içleri değiştirilebilir
sozluk = {}
sozluk = dict()
sozluksayi = {"sıfır":0,"bir":1,"iki":2,"üç":3}
print(sozluksayi)
print(sozluksayi["iki"])
 
s = {"bir" : [1,2,3,4], "iki": [[1,2],[3,4],[5,6]],"üç" : 15}
print(s)
print(s["iki"])
print(s["iki"][1][1]) 
s["üç"] += 10
print(s)

s= {"bir":1,"iki":2,"üç":3}
s["dört"] = 4 
 
print(s)

s = {"sayılar":{"bir":1,"iki":2,"üç":3},"meyveler":{"kiraz":"cherry","portakal":"orange","elma":"apple"}}
print(s)
 
sözlük = {"bir":1,"iki":2,"üç":3}
 
print(sözlük.values())
 
print(sözlük.keys())
 
print(sözlük.items())
# Sözlük çleri değiştirilebilir
s1 = {}
sozlukOgrenci = {"id": 1 ,"ad": "Şamil","soyad": "Yılmaz" ,"maas":2500}
sozlukManken = {"id":1 , "ad":"Ali" ,"Boy": 190 ,"Kilo":68}
print(sozlukOgrenci)
print(sozlukOgrenci["ad"])
sozlukOgrenci["maas"] += 1000
print(sozlukOgrenci)
print(sozlukOgrenci.values())
print(sozlukOgrenci.keys())
print(sozlukOgrenci.items())
