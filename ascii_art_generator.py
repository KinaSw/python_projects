import numpy as np
from PIL import Image

ASCII_CHARS = "@%#*+=-:. "

def resize_image(image, new_width=100):
    width, height = image.size
    ratio = height / width
    new_height = int(new_width * ratio * 0.55)
    return image.resize((new_width, new_height))

def grayify(image):
    if image.mode == 'RGBA':
        image = image.convert('RGB')
    return image.convert("L")


def pixels_to_ascii(image):
    pixels = np.array(image)
    ascii_str = ""
    for row in pixels:
        for pixel in row:
            index = int(pixel) * len(ASCII_CHARS) // 256
            ascii_str += ASCII_CHARS[index]

        ascii_str += "\n"
    return ascii_str

def main(path, width=100):
    try:
        image = Image.open(path)
    except:
        print("Nie mogę otworzyć tego pliku.")
        return

    image = resize_image(image, width)
    image = grayify(image)
    ascii_art = pixels_to_ascii(image)

    with open("ascii_output.txt", "w") as f:
        f.write(ascii_art)

    print(ascii_art)

if __name__ == "__main__":
    path = input("Podaj ścieżkę do pliku obrazu: ")
    main(path, width=120)
