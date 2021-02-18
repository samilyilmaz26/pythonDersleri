import seaborn as sea
import pandas as pd
hit = pd.read_csv("Hitters.csv")
 
print(hit)
dms = pd.get_dummies(hit[['League','Division','NewLeague']])
print(dms)
y= hit["Salary"]
x_ = hit.drop(["Salary",'League','Division','NewLeague'], axis=1).astype('float')
x= pd.concat([x_,dms[['League_N','Division_W','NewLeague_N']]], axis= 1)
print(x)
