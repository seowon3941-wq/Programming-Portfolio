import matplotlib.pyplot as plt
import numpy as np

plt.style.use('default')
plt.rcParams['figure.figsize'] = (12, 9)
plt.rcParams['font.size'] = 15

x = np.arange(0, 4)

y = [5.25, 4.44, 2.5, 3.485]
yerr = [0.05, 0.15, 0.5, 0.485]
y2 = [1.473, 1.522, 1.407, 0.546]

fig, ax1 = plt.subplots()

ax1.set_xlabel('fruit types')

ax1.set_ylabel('pH level(pH)', color='red') 
ax1.plot(x, y, marker='o', color='red', label='Error Bars Line')
ax1.errorbar(x, y, yerr=yerr, fmt='o', color='red', capsize=5)
ax1.set_xticks(x)  
ax1.set_xticklabels(['Watermelon', 'Kiwi', 'Lemon', 'Grapes'])  
ax1.set_ylim(0, 6) 

#ax2 = ax1.twinx()
#ax2.set_ylabel('electric pressure(V)', color='blue')
#ax2.plot(x, y2, marker='o', color='blue', label='Second Y Values')
#ax2.set_ylim(0, 2)

plt.savefig('savefig_default.png')