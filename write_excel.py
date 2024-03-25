import pandas as pd
data = {
    'Name':['Celyne', "Victor",'Jusmine'],
    'Age':[30,40,15],
    'Subject':["python","java","pandas"],
    "marks":[100,200,300]
}

df = pd.DataFrame(data)
writer = pd.ExcelWriter("myexcel.xlsx")
df.to_excel(writer, index = False)
writer._save()
