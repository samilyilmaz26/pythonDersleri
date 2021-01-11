import  seaborn as sea
tipsDf = sea.load_dataset("tips")
print(sea.scatterplot(x= "total_bill", y= "tip", data = tipsDf))