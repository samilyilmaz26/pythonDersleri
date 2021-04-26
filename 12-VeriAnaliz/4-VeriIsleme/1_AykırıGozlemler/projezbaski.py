 
import seaborn as sns
import pandas as pd

df = sns.load_dataset("diamonds")
 
df = df.select_dtypes(include= ["float64","int64"])
df = df.dropna()
 
df_table = df["table"]
sns.boxplot(x= df_table)
Q1 = df_table.quantile(0.25)
Q3 = df_table.quantile(0.75)
IQR = Q3-Q1
lowlimit = Q1-1.5*IQR
uplimit = Q3+ 1.5*IQR
 
ar_up = df_table>uplimit
ar_low = df_table<lowlimit
 
 
 

print(df_table[ar_low]) 
df_table[ar_low]   = lowlimit
print(df_table[ar_low]) 

print(df_table[ar_up])
df_table[ar_up]   = uplimit
print(df_table[ar_up])  
 
df_table = pd.DataFrame(df_table)
print(df_table<51.5)
 