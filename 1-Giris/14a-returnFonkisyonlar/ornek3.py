
def cellius(f):
    c = (f-32)/1.800
    return (round(c, 2))
fah  = float(input("Fahrenayt değeri ? "))
c = cellius(fah)
if c <10 :
    print('Hava Serin')
elif c <20 :
    print('Hava Ilık')
else:
    print('Hava Sıcak')
    
    
