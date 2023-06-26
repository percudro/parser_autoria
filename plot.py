import numpy as np
from numpy import sin
from numpy import arange
import pandas  as pd
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
from scipy.stats import gaussian_kde

def objective(x, a, b, c, d):
    return a * sin(b - x) + c * x**2 + d
 
headers = ['car', 'price', 'power']
df = pd.read_csv('cars.csv', names=headers)
x =  pd.to_numeric(df['power'])
y = pd.to_numeric(df['price'])
popt, _ = curve_fit(objective, x, y)
a, b, c, d = popt
xy = np.vstack([x,y])
z = gaussian_kde(xy)(xy)
fig, ax = plt.subplots()
ax.scatter(x, y, c=z, s=30)

x_line = arange(min(x), max(x), 20)
y_line = objective(x_line, a, b, c, d)
plt.plot(x_line, y_line, ':', color='red')
plt.show()