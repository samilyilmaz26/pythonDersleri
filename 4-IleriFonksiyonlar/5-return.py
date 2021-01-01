def fonksiyon(işlem_kodu):
    
    def toplama(*args):
        toplam = 0
        for i in args:
            toplam += i
        return toplam
        
    def çarpma(*args):
        çarpım = 1
        for i in args:
            çarpım *= i
        return çarpım
    
    if işlem_kodu == "+":
        return toplama
    else:
        return çarpma

       
toplam = fonksiyon("+")
print (type(toplam))
x = (toplam(1,2,3,4,5))
print(x)