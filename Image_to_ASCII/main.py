from PIL import Image
from colorama import Fore
import colorama

import numpy as np
import math

path = "Images/"
jpg = ".jpg"

gscale1 = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. "
gscale2 = '@%#*+=-:. '

im = Image.open(path + "khaled (1).png").convert("L")
im.save(path + "gray.png")

width, height = im.size
ratio = height / width

new_width = int(width * ratio)
new_height = int(height * ratio)
im = im.resize((new_width, new_height))

ramp_legth = len(gscale1)

grayscale_value = np.array(im)
w, h = grayscale_value.shape
avg = np.average(grayscale_value.reshape(w * h))

a = grayscale_value.reshape(w * h)
b = list(map(str, a))


def pixel_to_ascii():
    with open('ASCII.txt', 'w') as f:
        for index, value in enumerate(a):
            # print(index)
            if (index % new_width) == 0 and index != 0:
                f.write('\n')
                print('')
            if gscale1[math.ceil((ramp_legth - 1) * value / 255)] == '$':
                f.write(' ' + '')
                print(' ', end='')
            else:
                f.write(gscale1[math.ceil((ramp_legth - 1) * value / 255)] + '')
                print(gscale1[math.ceil((ramp_legth - 1) * value / 255)] + '', end='')
        print('\n')
        print(f"{new_width}x{new_height}")
        print(f"{width * ratio}x{height * ratio}")


if __name__ == '__main__':
    # pixel_to_ascii()
    pixel_to_ascii()
    print(Fore.RED + 'This text is red in color')
