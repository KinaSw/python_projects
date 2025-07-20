import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

n = 50
data = np.random.randint(1, 100, n)

fig, ax = plt.subplots()
bars = ax.bar(range(len(data)), data, align='edge')

ax.set_xlim(0, n)
ax.set_ylim(0, max(data)*1.1)
ax.set_title('Bubble Sort Visualization')

def bubble_sort(data):
    n = len(data)
    for i in range(n):
        for j in range(n-1-i):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
            yield data

def update(data):
    for bar, val in zip(bars, data):
        bar.set_height(val)
    return bars

ani = animation.FuncAnimation(fig, update, frames=bubble_sort(data.copy()), interval=50, repeat=False)
plt.show()
