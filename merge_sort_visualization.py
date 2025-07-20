import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

n = 50
data = np.random.randint(1, 100, n)

fig, ax = plt.subplots()
bars = ax.bar(range(len(data)), data, align='edge')

ax.set_xlim(0, n)
ax.set_ylim(0, max(data)*1.1)
ax.set_title('Merge Sort Visualization')

def merge_sort(data, left, right):
    if right - left > 1:
        mid = (left + right) // 2
        yield from merge_sort(data, left, mid)
        yield from merge_sort(data, mid, right)
        yield from merge(data, left, mid, right)
        yield data

def merge(data, left, mid, right):
    merged = []
    i, j = left, mid
    while i < mid and j < right:
        if data[i] < data[j]:
            merged.append(data[i])
            i += 1
        else:
            merged.append(data[j])
            j += 1
    while i < mid:
        merged.append(data[i])
        i += 1
    while j < right:
        merged.append(data[j])
        j += 1
    for i, val in enumerate(merged):
        data[left + i] = val
        yield data

def update(data):
    for bar, val in zip(bars, data):
        bar.set_height(val)
    return bars

generator = merge_sort(data.copy(), 0, len(data))
ani = animation.FuncAnimation(fig, update, frames=generator, interval=100, repeat=False)
plt.show()
