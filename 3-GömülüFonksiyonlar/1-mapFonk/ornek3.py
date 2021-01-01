liste1 = [1,2,3]
liste2 = [5,6,7]
liste3 = [8,9,10,11]
liste = list(map(lambda x,y,z : x * y * z , liste1,liste2,liste3))
print (liste)
