import sqlite3
con = sqlite3.connect("personel.db")
cursor = con.cursor() 

def Listele():
    cursor.execute('select * from personel')
    olist = cursor.fetchall()
    for i in olist:
        print(i)
def Ekle(ad,soyad,maas):
    cursor.execute('insert into personel (ad,soyad ,maas) values(? , ? ,?)', (ad,soyad,maas))
    con.commit()

def Guncel(id ,maas):
    cursor.execute('update  personel set maas = ?  where id =? ', (maas,id))
    con.commit()
 
def Sil(id ):
    cursor.execute('delete from   personel  where id =? ', (id,))
    con.commit()
 
 


