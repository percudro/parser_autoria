import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

headers = ['car', 'price', 'power']
csv = pd.read_csv('cars.csv', names=headers)
cars =  csv['car']
price = pd.to_numeric(csv['price'])

names = []

for car in cars:
    car = car.split(' ')[0]
    names.append(car)

csv['new_name'] = names

df = csv.groupby(['new_name']).mean().sort_values(by ='price')
print(df.head())
 
plt.bar(df.index.values, df['price'], color ='maroon', width = 0.4)
plt.xticks(rotation=40, ha='right')
plt.show()