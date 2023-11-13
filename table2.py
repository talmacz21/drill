import pandas as pd
# Load the CSV data into a DataFrame
df = pd.read_csv('table1.csv').dropna()
# Create a new column with calculated values
df['id'] = range(1,61)
# Write the updated DataFrame back to a CSV file
df.to_csv('table2.csv', index=False)
#add a new column  with prefix meta
df['date'] = 'META-'+df['date'].astype(str)

