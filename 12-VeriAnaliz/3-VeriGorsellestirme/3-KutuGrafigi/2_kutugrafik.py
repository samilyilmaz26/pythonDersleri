import  seaborn as sea
tipsDf = sea.load_dataset("tips")

print(sea.boxplot(x= tipsDf["total_bill"]))
