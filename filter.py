
import easygui
from tqdm import tqdm
import cv2
import numpy as np

def load_img():
    file = easygui.fileopenbox()

    img = cv2.imread(file)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    return gray

# Read the image
img = load_img()

# Obtain number of rows and columns
# of the image
m, n = img.shape

# Develop Averaging filter(3, 3) mask
mask = np.ones([3, 3], dtype=int)
mask = mask / 9

# Convolve the 3X3 mask over the image
img_new = np.zeros([m, n])


cv2.namedWindow("Display", cv2.WINDOW_AUTOSIZE)

for i in tqdm(range(1, m - 1)):
    for j in range(1, n - 1):
        #Iteration badness that is so cool that i donť remeber how it works
        temp = img[i - 1, j - 1] * mask[0, 0] + img[i - 1, j] * mask[0, 1] + img[i - 1, j + 1] * mask[0, 2] + img[
            i, j - 1] * mask[1, 0] + img[i, j] * mask[1, 1] + img[i, j + 1] * mask[1, 2] + img[i + 1, j - 1] * mask[
                   2, 0] + img[i + 1, j] * mask[2, 1] + img[i + 1, j + 1] * mask[2, 2]

        img_new[i, j] = temp
    img_show = img_new.astype(np.uint8)
    cv2.imshow('Display', img_show)
    cv2.waitKey(1)
cv2.waitKey(0)
cv2.destroyallwindows()

