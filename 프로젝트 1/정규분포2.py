import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import norm
import openpyxl

min_range = 1
max_range = 1

transparency = 0.3
colors = ['blue', 'orange', 'green']
labels = ['Basic FD KDE', 'Forward FD KDE', 'Reverse FD KDE'] 
data_columns = []

wb = openpyxl.load_workbook("C:/Users/Documents/data.xlsx")
sheet = wb["Sheet1"]

data = {}
for col, label in zip(data_columns, labels):
    data[col] = np.array([float(sheet[f"{col}{i}"].value) for i in range(min_range, max_range)])
    print (data[col])

all_data = np.concatenate(list(data.values()))
mean = np.mean(all_data)
std_dev = np.std(all_data)

x = np.linspace(mean - 3*std_dev, mean + 3*std_dev, 100)
pdf = norm.pdf(x, mean, std_dev)

plt.figure(figsize=(12, 8))

for col, color, label in zip(data_columns, colors, labels):
    sns.kdeplot(data[col], color=color, label=label, bw_adjust=0.5, alpha=transparency, shade=True)

plt.plot(x, pdf, 'r-', lw=2, label='Normal Distribution')

plt.xlabel('d (cm)', fontsize=15, loc='right')
plt.ylabel('Density', fontsize=15, loc='top')
plt.legend()
plt.grid(True)
plt.ylim([0, 0.03]) 

plt.savefig("s.jpg", bbox_inches="tight")
plt.show()
