import cv2
import numpy as np

# input image path

path = input('Input image path: ')

# loading image
img = cv2.imread(f'image/{path}', )

# converting to gray scale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# remove noise
img = cv2.GaussianBlur(gray, (3, 3), 0)

ddepth = cv2.CV_16S
kernel_size = 3

dst = cv2.Laplacian(img, ddepth, ksize=kernel_size)

cv2.imwrite(f'edge_processing_image/new1_builtin_{path}', dst)

abs_dst = cv2.convertScaleAbs(dst)


cv2.imshow("window_name", abs_dst)
cv2.waitKey(0)
