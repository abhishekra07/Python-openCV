import cv2
import numpy as np

img = cv2.imread("Resource/kingCard.jfif")

width, height = 250, 350

pts1 = np.float32([[132, 25], [234, 30], [122, 181], [223, 188]])
pts2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])
matrix = cv2.getPerspectiveTransform(pts1, pts2)
imgOutput = cv2.warpPerspective(img, matrix, (width, height))

print(img.shape)

cv2.imshow("Image", img)
cv2.imshow("Output Image", imgOutput)

# join two images
imgHorizontal = np.hstack((img, img))
imgVertical = np.vstack((img, img))

cv2.imshow("Horizontal Joining", imgHorizontal)
cv2.imshow("Vertical Joining", imgVertical)

cv2.waitKey(0)
