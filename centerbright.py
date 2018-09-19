import numpy as np
import cv2

name = input("Which image?")

img = cv2.imread(name,cv2.COLOR_BGR2HSV)
height = img.shape[0]
width = img.shape[1]
print("The shape of the image is:", img.shape)
center = img[int(3*height/8):int(5*height/8),int(3*width/8):int(5*width/8)]
h,s,v = cv2.split(center)
m = np.mean(v)

print("The processed 1/4 center shape is:", center.shape[:])
print("The center brightness of this image is:",int(m))


