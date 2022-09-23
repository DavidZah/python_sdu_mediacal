from random import random
import easygui
import cv2
import numpy as np

text_lst = ["COOL","NICE","HEY","SDU"]

height = 640
width = 820

blank_image = np.zeros((height,width,3), np.uint8)

font = cv2.FONT_HERSHEY_SIMPLEX

fontScale = 1
color = (255, 0, 0)
org = (50, 50)

thickness = 2

def load_img():
    file = easygui.fileopenbox()
    img_grayscale = cv2.imread(file)
    print(img_grayscale.shape)
    cv2.imshow('img', img_grayscale)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def screen_saver():
    while (True):
        random.randint(0,255)
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        # blank_image = np.zeros((height, width, 3), np.uint8)
        org = (random.randint(0, height), random.randint(0, width))
        # Using cv2.putText() method
        image = cv2.putText(blank_image, text_lst[random.randint(0, len(text_lst) - 1)], org, font,
                            fontScale, color, thickness, cv2.LINE_AA)

        cv2.imshow("Display", blank_image)
        cv2.waitKey(500)

screen_saver()