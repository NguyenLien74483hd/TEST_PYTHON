import cv2
import numpy as np

img=cv2.imread('Photo.jpg',cv2.IMREAD_GRAYSCALE)
cv2.imshow("anh",img)
cv2.waitKey()
img_binary=cv2.adaptiveThreshold(img, maxValue=255, adaptiveMethod= cv2.ADAPTIVE_THRESH_MEAN_C,
                                 thresholdType=cv2.THRESH_BINARY, blockSize=15, C=8)
cv2.imshow("anh nhi phan:",img_binary)
cv2.waitKey()
