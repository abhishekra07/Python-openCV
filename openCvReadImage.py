import cv2  # importing computer vision module
import numpy as np

img = cv2.imread("Resource/lady.jfif")  # reading or loading image

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # converting image to gray color space. openCV follow BGR color pattern
imgBlur = cv2.GaussianBlur(imgGray, (3, 3), 0)  # ksize should be odd numbers
imgCanny = cv2.Canny(img, 150, 200)  # to detect edges in image

kernal = np.ones((5, 5), np.uint8)
imgDialation = cv2.dilate(imgCanny, kernal, iterations=1)

imgEroded = cv2.erode(imgDialation, kernal, iterations=1)

cv2.imshow("Gray image Window", imgGray)
cv2.imshow("Blur image Window", imgBlur)  # display image
cv2.imshow("Canny image Window", imgCanny)
cv2.imshow("Dialation image Window", imgDialation)
cv2.imshow("Erode image Window", imgEroded)

cv2.waitKey(0)  # add delay so we can see image
