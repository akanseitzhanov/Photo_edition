import numpy as np
import matplotlib.pyplot as plt
import cv2

def image_smoother(imagePointer):
img = cv2.imread('/Users/Lenovo/Desktop/photo2.jpg')
height = len(img)
width = len(img[0])

b = np.array([0.3,0.59,0.11])
img2 = np.dot(img[:][:],b)
img3 = np.ndarray(shape=(height, width))

for i in range(0, height,1):
    for j in range(0, width,1):
        img3[i:i+3,j:j+3] = np.mean(img2[i:i+3,j:j+3])
print(img3)



cv2.imwrite('smooth_image.jpeg', img3)
plt.imshow(img3)
plt.show()


image_smoother('/Users/Lenovo/Desktop/photo2.jpg')
