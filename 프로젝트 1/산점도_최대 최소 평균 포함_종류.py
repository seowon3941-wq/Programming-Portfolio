import openpyxl
import numpy as np
import matplotlib.pyplot as plt

wb = openpyxl.load_workbook("C:/Users/Documents/data.xlsx")
sheet = wb["Sheet1"]

size = 10
d_color = 'blue'
min_range = 1
max_range = 1
x_lad = [1, 2, 3]
columns = []
labels = ['','Basic FD', 'Forward FD', 'Reverse FD','']
means = []
max_vals = []
min_vals = []


for i, col in enumerate(columns):
    Y = [float(sheet[f"{col}{row}"].value) for row in range(min_range, max_range)]
    X = [i + 1 for _ in range(len(Y))]  
    
    plt.scatter(X, Y, s=size, color=d_color)

    min_val = min(Y)
    max_val = max(Y)
    mean_val = sum(Y) / len(Y)

    plt.scatter(x_lad[i], mean_val, s=size, color='blue')  
    plt.scatter(x_lad[i], max_val, s=size, color='green')  
    plt.scatter(x_lad[i], min_val, s=size, color='red')   
    min_vals.append(min_val)
    max_vals.append(max_val)
    means.append(mean_val)


plt.plot(x_lad, min_vals, 'r-', label='Minimum')
plt.plot(x_lad, max_vals, 'g-', label='Maximum')
plt.plot(x_lad, means, '--', label='Mean')
plt.title('')  
plt.ylim([0, 320]) 
plt.grid(True)
plt.xlabel('θ(˚)', fontsize=15, loc='right')
plt.ylabel('d(cm)', fontsize=15, loc='top')
plt.legend()
plt.xticks(ticks=np.arange(0, len(labels)), labels=labels)

plt.savefig("s.jpg", bbox_inches="tight")
plt.show()
