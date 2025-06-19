import pandas as pd
import numpy as np
# 1
data = pd.read_csv('cities.csv')

# 2
print(data.isnull().sum().sum())
data.columns = data.columns.str.replace('"', '').str.strip()
data = data.dropna(axis=0)

# 3
population = np.random.choice(10000,len(data))
data['population'] = population
average_population = data.groupby("City")["population"].mean().reset_index()
print (average_population)
print (data['population'].max())
print (data['population'].min())

# 4
area = np.random.choice(10000,len(data))
data['area'] = area

data['ratio'] = data['population']/data['area']
data.rename(columns={'population': 'Population'}, inplace=True)

# 5
print (data.loc[data['City']=='Youngstown', :])
data = data.sort_values(by='Population', ascending=False)

# 6
data.to_csv('changed_cities.csv', index=False)