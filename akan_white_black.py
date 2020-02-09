import numpy as np
import matplotlib.pyplot as plt
import cv2

def image_processor(imagePointer):
    img = cv2.imread(imagePointer)
    height = len(img)
    width = len(img[0])

    b = np.array([0.3,0.59,0.11])
    img2 = np.dot(img[:][:],b)
    print(img2.shape)
    cv2.imwrite('res.jpeg', img2)
    plt.imshow(img2)
    plt.show()

    height = len(img2)
    width = len(img2[0])

    img3 = np.ndarray(shape=(height, width))

    for i in range(0,height):
        for j in range(0,width):
            if img2[i][j] > 105:
                img3[i][j] = 255
            elif img2[i][j] < 105:
                img3[i][j] = 0

    cv2.imwrite('white_black_image.jpeg', img3)
    plt.imshow(img3)
    plt.show()


image_processor('/Users/Lenovo/Desktop/photo2.jpg')

