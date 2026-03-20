import matplotlib.pyplot as plt
import numpy as np

x = np.array(['Watermelon', 'Kiwi', 'Lemon', 'Grapes'])
y1 = np.array([

1/0.038,
1/0.098,
1/0.03,
1/0.718

])
y2 = np.array([1.473, 1.522, 1.407, 0.546])

plt.style.use('default')
plt.rcParams['figure.figsize'] = (12, 9)
plt.rcParams['font.size'] = 15


fig, ax1 = plt.subplots()
ax1.set_xlabel('fruit types')
ax1.set_ylabel('1/Mn(mg)', color='red')
ax1.plot(x, y1, color='red', label='y1')
ax1.set_ylim(0, 50) 

ax2 = ax1.twinx()
ax2.set_ylabel('electric pressure(V)', color='blue')
ax2.plot(x, y2, color='blue', label='y2')
ax2.set_ylim(0, 2)

plt.savefig('savefig_default_3.png')