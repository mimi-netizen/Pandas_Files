import pandas as pd
data = {
    'Name':['Celyne', "Victor",'Jusmine'],
    'Age':[30,40,15],
    'Subject':["python","java","pandas"],
    "marks":[100,200,300]
}

df = pd.DataFrame(data)
df.to_json("myjson.json", orient = "records")