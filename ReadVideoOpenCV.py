import cv2  # importing computer vision module

cap = cv2.VideoCapture("Resource/big_buck_bunny.mp4")  # reading video

while True:
    success, img = cap.read()  # read image as video is nothing but sequence/frame of images. success flag indicate
    # whether image is captured successfully or not

    cv2.imshow("Video Window", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):  # adding delay and if q key is pressed exit loop
        break
