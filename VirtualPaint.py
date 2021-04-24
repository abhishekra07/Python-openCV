import cv2  # importing computer vision module
import numpy as np

myColors = [[139, 122, 44, 179, 255, 255],
            [29, 107, 147, 46, 254, 255]]

colors = [[167, 11, 214], [10, 255, 202]]

drawLinePoints = []  # [ x, y, colorIndex]

def empty(a):
    pass


def find_color(img):
    count = 0
    newPoints = []
    for color in myColors:
        imgHsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        lower = np.array(color[0:3])
        upper = np.array(color[3:6])
        mask = cv2.inRange(imgHsv, lower, upper)
        x, y = get_contours(mask)
        cv2.circle(imgResult, (x, y), 10, colors[count], cv2.FILLED)
        # cv2.imshow(str(color[0]), mask)
        if x != 0 and y != 0:
            newPoints.append([x, y, count])
        count += 1
    return newPoints


def get_contours(img):
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    x, y, w, h = 0, 0, 0, 0
    for contour in contours:
        area = cv2.contourArea(contour)
        print(area)
        if area > 100:
            # cv2.drawContours(imgResult, contour, -1, (255, 194, 3), 2)
            peri = cv2.arcLength(contour, True)
            approx = cv2.approxPolyDP(contour, 0.02 * peri, True)
            x, y, w, h = cv2.boundingRect(approx)
    return x + w // 2, y

def draw_on_cavas(drawPoints):
    for point in drawPoints:
        cv2.circle(imgResult, (point[0], point[1]), 30, colors[point[2]], cv2.FILLED)


cap = cv2.VideoCapture(0)  # reading video from webcam. just give id of webcam
cap.set(3, 640)  # width
cap.set(4, 480)  # height
cap.set(10, 150)  # brightness

while True:
    success, img = cap.read()  #
    imgResult = img.copy()
    newPoints = find_color(img)
    if len(newPoints) > 0:
        for point in newPoints:
            drawLinePoints.append(point)

    if len(drawLinePoints) > 0:
        draw_on_cavas(drawLinePoints)

    cv2.imshow("Video Window", imgResult)

    if cv2.waitKey(1) & 0xFF == ord('q'):  # adding delay and if q key is pressed exit loop
        break
