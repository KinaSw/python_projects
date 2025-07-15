from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# PART I
#image = np.zeros((100, 100))
#image[30:70, 45:55] = 1  # biały prostokąt w środku

# Wczytaj obrazek i przekształć do skali szarości
img = Image.open("./cat.png").convert('L')  # 'L' = grayscale
image = np.array(img)

# Rozmiar płótna na animację
diag = int(np.ceil(np.sqrt(image.shape[0]**2 + image.shape[1]**2)))
canvas = np.zeros((diag, diag))

# PART II
def rotate_image(canvas, image, angle_rad):
    """
    Obraca obrazek `image` o zadany kąt (w radianach), wpisując go w centrum `canvas`.

    Parametry:
    - canvas: tablica wyjściowa (większa, kwadratowa)
    - image: tablica źródłowa (mniejsza)
    - angle_rad: kąt obrotu w radianach

    Zwraca:
    - nowy canvas z obróconym i wycentrowanym obrazkiem
    """

    # Krok 1: rozmiary obrazków
    h, w = image.shape
    H, W = canvas.shape

    # Krok 2: środki obrazków
    cx, cy = w/2, h/2
    new_cx, new_cy = W/2, H/2

    # Krok 3: utworzenie siatki współrzędnych płótna
    y_indices, x_indices = np.indices((W,H))

    # Krok 4: przesunięcie współrzędnych względem środka płótna
    x_shifted = x_indices - new_cx
    y_shifted = y_indices - new_cy

    # Krok 5: obliczenie współrzędnych oryginalnych (po odwrotnej rotacji)
    cos_a = np.cos(-angle_rad)
    sin_a = np.sin(-angle_rad)

    # TODO: uzupełnij wzory x_orig i y_orig
    x_orig = cos_a * y_shifted - sin_a * x_shifted + cx
    y_orig = sin_a * y_shifted + cos_a * x_shifted + cy

    # Krok 6: zaokrąglenie współrzędnych do najbliższego piksela
    x_orig = np.round(x_orig).astype(int)
    y_orig = np.round(y_orig).astype(int)

    # Krok 7: filtr – tylko punkty mieszczące się w granicach oryginalnego obrazka
    # TODO: uzupełnij warunek maski
    mask = (
        (x_orig >= 0) & (x_orig < w) & (y_orig >= 0) & (y_orig < h)
    )

    # Krok 8: przypisanie pikseli z image do canvas
    rotated = np.zeros_like(canvas)
    # TODO: użyj maski do przypisania wartości
    rotated[mask] = image[y_orig[mask], x_orig[mask]]

    # Krok 9: zwróć wynik
    return rotated

# PART III
# Animacja
def evolve(frame_num, canvas, image):
    angle = np.deg2rad(frame_num)
    rotated = rotate_image(canvas, image, angle)
    mat.set_data(rotated)
    return [mat]

fig, ax = plt.subplots()
mat = ax.matshow(rotate_image(canvas, image, 0))
ani = animation.FuncAnimation(fig, evolve, frames=360, fargs=(canvas, image), interval=20)
plt.show()
