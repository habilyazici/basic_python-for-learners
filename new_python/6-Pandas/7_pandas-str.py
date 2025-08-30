import pandas as pd
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

data = pd.read_csv("datasets/nba.csv")
data.dropna(inplace = True)

data["Name"] = data["Name"].str.lower()
data["index"] = data["Name"].str.find('a')
data['Team'] = data['Team'].str.replace(' ','-')
print(data.columns)
print("\n" + 20 * '-' + "\n")

print('hor içeren nameler:\n', data[data['Name'].str.contains('hor')])
print("\n" + 20 * '-' + "\n")

# .loc[] ile içerisindeki koşulları sağlayan satırları seçiyoruz.
data[['FirstName','LastName']] = data['Name'].loc[data['Name'].str.split().str.len()==2].str.split(expand=True)

print(data.sample(5))