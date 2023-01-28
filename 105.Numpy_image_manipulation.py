
import numpy as np
import skimage.io
import matplotlib.pyplot as plt

from skimage import io
#Import an Image into Python with Skimage imread
#image processing function

camaro = io.imread("camaro.jpg")
print(camaro)

camaro.shape

plt.imshow(camaro)
plt.show()

# slicing the arrays in order to crop the image
#cropping the image

cropped = camaro[0:500,:,:]
plt.imshow(camaro)
plt.show()

cropped = camaro[:,400:1000,:]
plt.imshow(camaro)
plt.show()

cropped = camaro[350:1100,200:1400,:]
plt.imshow(camaro)
plt.show()
io.imsave("camaro_cropped.jpg",cropped)
#flip our image


vertical_flip = camaro[::-1,:,:]
plt.imshow(vertical_flip)
plt.show()
io.imsave("camaro_vertical_flip.jpg",vertical_flip)

horizontal_flip = camaro[::-1,:,:]
plt.imshow(horizontal_flip)
plt.show()

io.imsave("camaro_horizontal_flip.jpg",horizontal_flip)

#colour channels
# create the array with size of the original image

#create red channel

red = np.zeros(camaro.shape, dtype = "uint8")
red[:,:,0] = camaro[:,:,0]
plt.imshow(red)
plt.show()

#change of colour= change of canal
green = np.zeros(camaro.shape, dtype = "uint8")
green[:,:,1] = camaro[:,:,1]
plt.imshow(green)
plt.show()

blue = np.zeros(camaro.shape, dtype = "uint8")
blue[:,:,2] = camaro[:,:,2]
plt.imshow(blue)
plt.show()

#numpy.vstack() function is used to stack the sequence of input arrays vertically to make a single array
camaro_rainbow = np.vstack((red, green, blue))
plt.imshow(camaro_rainbow)
plt.show()

io.imsave("camaro_rainbow.jpg",camaro_rainbow)