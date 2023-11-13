import pandas as pd 
import random 
# Load the CSV data into a DataFrame
df = pd.read_csv('table1.csv').dropna()
# Create a new column with calculated values
df['id'] = range(1,61)
# Write the updated DataFrame back to a CSV file

#add a new column  with prefix meta

df['Date']='META-'+ df['Date']
print(df)
#add a new column with randomly assigned 0,1

dummy = []
for c in range (0,60):
    r = random.randint(0,1)
    dummy.append(r)
df['random'] =dummy 
print(df)
# Transpose the rows as columns
transposed_df = df.transpose()
print(transposed_df)
df.to_csv('table2.csv', index=False)
transposed_df.to_csv('table3.csv', index=False)
