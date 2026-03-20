import openpyxl
import numpy as np
import matplotlib.pyplot as plt

wb = openpyxl.load_workbook("C:/Users/Documents/data.xlsx")
sheet = wb["Sheet1"]

size = 10
d_color = 'blue'
min_range = 2
max_range = 101
columns = ['A', 'B', 'C']
labels = ['θ=0˚', 'θ=6˚', 'θ=12˚']  

for i, col in enumerate(columns):
    Y = [float(sheet[f"{col}{row}"].value) for row in range(min_range, max_range)]
    X = [i + 1 for _ in range(len(Y))]  
    
    plt.scatter(X, Y, s=size, color=d_color, label=labels[i])

plt.title('')  
plt.ylim([0, 320]) 
plt.grid(True)
plt.xlabel('θ(˚)', fontsize=15)
plt.ylabel('d(cm)', fontsize=15)
plt.legend()
plt.xticks(ticks=np.arange(1, len(labels)+1), labels=labels)
plt.savefig("s.jpg", bbox_inches="tight")
plt.show()