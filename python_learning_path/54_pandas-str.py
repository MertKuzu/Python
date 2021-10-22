import pandas as pd

data = pd.read_csv("54.2_nba.csv")
data.dropna(inplace=True)

# data["Name"] = data["Name"].str.upper()
# data["Name"] = data["Name"].str.lower()
# data["index"] = data["Name"].str.find("a")
# data = data[data.Name.str.contains("jordan")]
# data = data.Team.str.replace(" ", "-")

data[["FirstName","LastName"]] = data['Name'].loc[data['Name'].str.split().str.len()==2].str.split(expand = True)

print(data)