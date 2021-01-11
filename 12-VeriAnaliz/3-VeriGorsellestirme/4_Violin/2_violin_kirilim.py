import  seaborn as sea
tipsDf = sea.load_dataset("tips")

print(sea.catplot(x= "day",y= "total_bill",kind="violin",  data=tipsDf))
print(sea.catplot(x= "day",y= "total_bill",kind="violin", hue="sex", data=tipsDf))