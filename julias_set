import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

s = 1000
x = np.linspace(-1.5, 1.5, s)
y = np.linspace(-1.5, 1.5, s)
X, Y = np.meshgrid(x, y)
Z = X + 1j * Y

def julia(z, c, max_iter=200):
    z = z.copy()
    man = np.zeros(z.shape, dtype=int)
    mask = np.ones(z.shape, dtype=bool)
    for i in range(max_iter):
        z[mask] = z[mask] ** 2 + c
        escaped = np.abs(z) > 2
        man[mask & escaped] = i
        mask &= ~escaped
        if not mask.any():
            break
    man[mask] = max_iter
    return man

def main():
    A, B = 0.7885, 0.7885
    a, b = 3, 2
    delta = np.pi / 2
    total_frames = 720

    fig, ax = plt.subplots()
    c = A * np.sin(a * 0 + delta) + 1j * B * np.cos(b * 0)
    mat = ax.matshow(julia(Z, c), cmap='magma')

    def evolve(frame):
        phi = frame / total_frames * 4 * np.pi
        re = A * np.sin(a * phi + delta)
        im = B * np.cos(b * phi)
        c = re + 1j * im
        man = julia(Z, c)
        mat.set_data(man)
        return [mat]

    ani = animation.FuncAnimation(fig, evolve, frames=total_frames, interval=20, blit=True)
    plt.show()

if __name__ == "__main__":
    main()
