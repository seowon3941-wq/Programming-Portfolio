import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
import openpyxl

wb = openpyxl.load_workbook("C:/Users/Documents/data.xlsx")
sheet = wb["Sheet1"]
transparency = 0.3

min_range = 2
max_range = 101

data_columns = ['A', 'B', 'C']
labels = ['Basic FD KDE', 'Forward FD KDE', 'Reverse FD KDE']
colors = ['blue', 'orange', 'green']

data = {}
for col, label in zip(data_columns, labels):
    data[col] = np.array([float(sheet[f"{col}{i}"].value) for i in range(min_range, max_range)])

all_data = np.concatenate(list(data.values()))
mean = np.mean(all_data)
std_dev = np.std(all_data)
x = np.linspace(mean - 3*std_dev, mean + 3*std_dev, 100)
pdf = norm.pdf(x, mean, std_dev)
plt.plot(x, pdf, 'r-', lw=2, label='Normal Distribution')

plt.xlabel('d (cm)', fontsize=15)
plt.ylabel('Density', fontsize=15)
plt.legend()
plt.grid(True)
plt.ylim([0, 0.02])

plt.savefig("s.jpg", bbox_inches="tight")
plt.show()