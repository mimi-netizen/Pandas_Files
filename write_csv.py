import pandas as pd
data = {
    'Name':['Celyne', "Victor",'Jusmine'],
    'Age':[30,40,15],
    'Subject':["python","java","pandas"],
    "marks":[100,200,300]
}

df = pd.DataFrame(data)
csv_file = df.to_csv("mycsv.csv")
reading_csv = pd.read_csv("mycsv.csv")
print(reading_csv)