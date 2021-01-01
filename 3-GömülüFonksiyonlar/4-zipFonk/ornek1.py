liste1 = [1,2,3,4,5]
liste2 = [6,7,8,9,10,11]
liste = list (zip(liste1,liste2))
print(liste)
for i,j in zip(liste1,liste2):
    print(i,j)
