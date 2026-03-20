import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import openpyxl

min_range = 2
max_range = 101
transparency = 0.3
colors = ['blue', 'orange', 'green']
labels = ['θ=0˚ KDE', 'θ=6˚ KDE', 'θ=12˚ KDE']
data_columns = ['A', 'B', 'C']

wb = openpyxl.load_workbook("C:/Users/Documents/data.xlsx")
sheet = wb["Sheet1"]

data = {}
for col, label in zip(data_columns, labels):
    data[col] = np.array([float(sheet[f"{col}{i}"].value) for i in range(min_range, max_range)])
    print(data[col])

fig, axes = plt.subplots(1, 3, figsize=(18, 6), sharey=True)

for ax, col, color, label in zip(axes, data_columns, colors, labels):
    sns.kdeplot(data[col], color=color, label=label, bw_adjust=0.5, alpha=transparency, fill=True, ax=ax)
    ax.set_xlabel('d (cm)', fontsize=15)
    ax.set_ylabel('Density', fontsize=15)
    ax.legend()
    ax.grid(True)
    ax.set_ylim([0, 0.03])
    ax.set_xlim([0, 300])

plt.savefig("s.jpg", bbox_inches="tight")
plt.show()