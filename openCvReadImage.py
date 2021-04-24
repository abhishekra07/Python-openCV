import cv2  # importing computer vision module

img = cv2.imread("Resource/man.png")  # reading or loading image

cv2.imshow("Image Window", img)  # display image

cv2.waitKey(0)  # add delay so we can see image
