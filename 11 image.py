import numpy as np
import matplotlib.pyplot as plt

from PIL import Image
# pip install pillow

img = Image.open('999.jpg')

# fig = plt.figure(figsize=(6, 4))
# ax = fig.add_subplot()
# axmshow(img)

plt.imshow(img)

plt.show()