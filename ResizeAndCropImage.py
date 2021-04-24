import cv2  # importing computer vision module

img = cv2.imread("Resource/lady.jfif")  # reading or loading image

print(img.shape)  # (183 -> height, 275 -> width, 3 -> colors(BGR))

imgResize = cv2.resize(img, (200, 150))  # (200 -> width, 150 -> height)
print(imgResize.shape)  # (150, 200, 3)

imgCropped = img[0:150, 50:200]  # height,width
print(imgCropped.shape)  # (150, 150, 3)

cv2.imshow("image Window", img)
cv2.imshow("Resized image Window", imgResize)
cv2.imshow("Cropped image Window", imgCropped)

cv2.waitKey(0)  # add delay so we can see image
