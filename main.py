import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv
import os
from copy import copy


def remove_background(image):
    image_hsv = cv.cvtColor(image, cv.COLOR_BGR2HSV)

    # Remove any saturation value that is less than 127
    saturation = image_hsv[:, :, 1]
    saturation = np.where(saturation < 127, 0, 1)

    # Increase the brightness of the image and then mod by 255 to keep a part of brightness
    value = (image_hsv[:, :, 2] + 127) % 255
    value = np.where(value > 127, 1, 0)  # Values that are above 127 will be accepted

    # Combining two masks based on Saturation and Value into a Foreground
    foreground = np.where(saturation + value > 0, 1, 0).astype(np.uint8)

    background = np.where(foreground == 0, 0, 255).astype(np.uint8)
    background = cv.cvtColor(background, cv.COLOR_GRAY2BGR)
    foreground = cv.bitwise_and(image, image, mask=foreground)
    final_image = background + foreground

    return final_image


def separate_leaf_core(image, counter):
    main_image = copy(image)
    new_image = remove_background(image)
    gray_image = cv.cvtColor(new_image, cv.COLOR_BGR2GRAY)
    (T, thresh) = cv.threshold(gray_image, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
    kernel = cv.getStructuringElement(cv.MORPH_ELLIPSE, (4, 4))
    opening = cv.morphologyEx(thresh, cv.MORPH_OPEN, kernel)
    leaf = cv.bitwise_and(main_image, main_image, mask=opening)
    file_name = "Leaf " + str(counter + 1) + ".png"
    cv.imwrite(file_name, leaf)
    images = [main_image, new_image, opening, leaf]
    titles = ['1-Original Image', '2-Removed Background Image', '3-Generated Mask', '4-Final Result']
    plt.figure(1).set_figheight(15)
    plt.figure(1).set_figwidth(15)
    for i in range(4):
        plt.subplot(2, 2, i + 1),
        if i == 0:
            plt.imshow(cv.cvtColor(images[i], cv.COLOR_BGR2RGB))
        elif i == 1 and i == 2:
            plt.imshow(images[i], cmap='gray')
        else:
            plt.imshow(cv.cvtColor(images[i], cv.COLOR_BGR2RGB))
        plt.title(titles[i], fontsize=25)
        plt.xticks([]), plt.yticks([])
    plt.show()



path = "images"
images_list = os.listdir(path)
for i in range(len(images_list)):
    file_path = path + "/" + images_list[i]
    img = cv.imread(file_path)
    separate_leaf_core(img, i)
