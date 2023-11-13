import csv

with open("./table1.csv", 'r') as file:
  csvreader = csv.reader(file)
  for row in csvreader:
    print(row)
  # add a new column to each row 
  for row in rows:
    row.append('id')
  #write the updated rows back to a CSV file
  with open (table1.csv,'w', newline='')as f:
    writer=csv.writer(f)
    writer.writerows(rows)
    