import numpy as np
import matplotlib.pyplot as plt
import cv2

def image_lightening_effect(imagePointer):
    img = cv2.imread(imagePointer)

    height = len(img)
    width = len(img[0])

    b, g, r = cv2.split(img)
    colors = [b, g, r]
    hist_b = np.histogram(b.flatten(), 256, [0, 256])
    hist_g = np.histogram(g.flatten(), 256, [0, 256])
    hist_r = np.histogram(r.flatten(), 256, [0, 256])

# plt.bar(range(len(hist_b[0])), hist_b[0])
# plt.show()
#
# plt.bar(range(len(hist_g[0])), hist_g[0])
# plt.show()
#
# plt.bar(range(len(hist_g[0])), hist_g[0])
# plt.show()


    cumsum_blue= np.cumsum(hist_b[0])
    cumsum_green= np.cumsum(hist_g[0])
    cumsum_red= np.cumsum(hist_r[0])

# print(cumsum_blue)
    new_hist_blue = np.ndarray( shape=len(cumsum_blue))
    new_hist_green = np.ndarray( shape=len(cumsum_green))
    new_hist_red = np.ndarray( shape=len(cumsum_red))

    for i in range(0,len(cumsum_blue)):
        new_hist_blue[i] = 255*(cumsum_blue[i] - min(cumsum_blue))/(max(cumsum_blue)-min(cumsum_blue))

# print(new_hist_blue)

# plt.bar(range(len(new_hist_blue)), new_hist_blue)
# plt.show()

    for i in range(0,len(cumsum_green)):
        new_hist_green[i] = 255*(cumsum_green[i] - min(cumsum_green))/(max(cumsum_green)-min(cumsum_green))

# print(new_hist_green)

# plt.bar(range(len(new_hist_green)), new_hist_green)
# plt.show()

    for i in range(0,len(cumsum_red)):
        new_hist_red[i] = 255*(cumsum_red[i] - min(cumsum_red))/(max(cumsum_red)-min(cumsum_red))

    new_img_blue = np.ndarray(shape=(height, width))
    new_img_green = np.ndarray(shape=(height, width))
    new_img_red = np.ndarray(shape=(height, width))

    for i in range(0,height):
        for j in range(0,width):
            new_img_blue[i][j] =  new_hist_blue[b[i][j]]
            new_img_green[i][j] =  new_hist_green[g[i][j]]
            new_img_red[i][j] =  new_hist_red[r[i][j]]


    new_image_rgb = np.ndarray(shape=(height, width,3))


    for i in range(0,height):
        for j in range(0,width):
            new_image_rgb[i][j][0] = new_img_blue[i][j]
            new_image_rgb[i][j][1] = new_img_green[i][j]
            new_image_rgb[i][j][2] = new_img_red[i][j]

    print(new_image_rgb.shape)

    cv2.imwrite('effect.jpeg', new_image_rgb)
    plt.imshow(new_image_rgb)
    plt.show()

image_lightening_effect('/Users/Lenovo/Desktop/photo3.jpg')
