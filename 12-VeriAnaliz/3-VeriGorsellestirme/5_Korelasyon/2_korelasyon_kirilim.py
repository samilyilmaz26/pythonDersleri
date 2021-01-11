import  seaborn as sea
tipsDf = sea.load_dataset("tips")
print(sea.scatterplot(x= "total_bill", y= "tip",hue="time" ,data = tipsDf))
print(sea.scatterplot(x= "total_bill", y= "tip",hue="time",style="time" ,data = tipsDf))
print(sea.scatterplot(x= "total_bill", y= "tip",hue="day",style="day" ,data = tipsDf))
print(sea.scatterplot(x= "total_bill", y= "tip",hue="size",size="size" ,data = tipsDf))
print(sea.scatterplot(x= "total_bill", y= "tip",size="size" ,data = tipsDf))