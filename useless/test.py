import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('test22.jpg',1)
cv2.imshow('image',img)
'''
cv2.imshow("r", img[:,:,0])
cv2.imshow("g", img[:,:,1])
cv2.imshow("b", img[:,:,2])

'''
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
#cv2.imshow("h", img_hsv[:,:,0])
#cv2.imshow("s", img_hsv[:,:,1])
#cv2.imshow("v", img_hsv[:,:,2])





#img = cv2.imread('test22.jpg',0)
img_r = img_hsv[:,:,2]
img_r = img[:,:,0]
edges = cv2.Canny(img_r,100,150)

plt.subplot(121),plt.imshow(img_r,cmap = 'gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(edges,cmap = 'gray')
plt.title('Edge Image'), plt.xticks([]), plt.yticks([])

plt.show()
