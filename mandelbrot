from multiprocessing import Pool, cpu_count
import matplotlib.pyplot as plt
import numpy as np
from time import time

x = np.linspace(-2, 1, 200)
y = np.linspace(-1.5, 1.5, 200)
x, y = np.meshgrid(x, y)
z = x + 1j * y

def mandel(z):
    p = np.copy(z)
    res = 255 * np.ones(z.shape)
    for i in range(255):
        mask = (np.abs(z) > 2) & (res == 255)
        res[mask] = i
        z = z**2 + p
    return res

def worker(z_part):
    return mandel(z_part)

def main():
    start = time()
    n = cpu_count()
    parts = np.array_split(z, n, axis=1)

    with Pool(processes=n) as pool:
        results = pool.map(worker, parts)

    mandel_all = np.hstack(results)

    plt.imshow(mandel_all)
    print(time() - start)
    plt.show()

if __name__ == "__main__":
    main()
