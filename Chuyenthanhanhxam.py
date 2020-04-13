import cv2
import numpy as np

img=cv2.imread('Photo.jpg',cv2.IMREAD_GRAYSCALE)
cv2.imshow('noi dung anh can hien thi',img)
cv2.waitKey()
cv2.imwrite('anh_xam_123.jpg',img)
