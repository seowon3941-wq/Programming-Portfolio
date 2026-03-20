import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
from openpyxl.drawing.image import Image
import openpyxl
min_range = 25
max_range = 36
wb = openpyxl.load_workbook("C:/Users/Alex/Documents/data.xlsx")


sheet = wb["Sheet1"]
last_row = len(sheet["A"])
size = 10
d_color = 'blue'

data1 = np.array([float(sheet["P{}".format(i)].value) for i in range(min_range, max_range)])
data2 = np.array([float(sheet["S{}".format(i)].value) for i in range(min_range, max_range)])
data3 = np.array([float(sheet["V{}".format(i)].value) for i in range(min_range, max_range)])

all_data = np.concatenate([data1, data2, data3])

mean = np.mean(all_data)
std_dev = np.std(all_data)

x = np.linspace(mean - 3*std_dev, mean + 3*std_dev, 100)

pdf = norm.pdf(x, mean, std_dev)

plt.figure(figsize=(12, 8))

plt.hist(data1, bins=10, density=True, alpha=0.6, color='blue', edgecolor='black', label='θ=0˚ Histogram')

plt.hist(data2, bins=10, density=True, alpha=0.6, color='orange', edgecolor='black', label='θ=6˚ Histogram')

plt.hist(data3, bins=10, density=True, alpha=0.6, color='green', edgecolor='black', label='θ=12˚ Histogram')


plt.plot(x, pdf, 'r-', lw=2, label='Normal Distribution')

plt.xlabel('d(cm)', fontsize = 15, loc='right')
plt.ylabel('Density', fontsize = 15, loc='top')
plt.ylim([0, 0.2]) 
plt.legend()
plt.grid(True)
plt.savefig("s.jpg", bbox_inches="tight")
plt.show()
