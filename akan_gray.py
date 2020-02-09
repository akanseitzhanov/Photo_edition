import numpy as np
import matplotlib.pyplot as plt
import cv2

def image_gray_maker(ImagePointer):
    img = cv2.imread(ImagePointer)
    height = len(img)
    width = len(img[0])


    b = np.array([0.3,0.59,0.11])
    img2 = img[:][:]*b

    for i in range(0,height):
        for j in range(0,width):
            img2[i][j] = img2[i][j][0]+img2[i][j][1]+img2[i][j][2]
    print(img2.shape)

    cv2.imwrite('gray_image.jpeg', img2)
    plt.imshow(img2.astype('uint8'))
    plt.show()

image_gray_maker('/Users/Lenovo/Desktop/photo2.jpg')