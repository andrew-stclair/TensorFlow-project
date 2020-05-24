import tensorflow as tf
import cv2

video = cv2.VideoCapture(1)

cv2.namedWindow("input")

img_counter = 0

while True:
    ret, frame = video.read()
    cv2.imshow("input", frame)
    if not ret:
        break
    k = cv2.waitKey(1)

    if k % 256 == 27:
        # ESC Pressed
        break
    elif k % 256 == 32:
        # SPACE pressed
        img_name = "opencv_frame_{}.png".format(img_counter)
        cv2.imwrite(img_name, frame)
        img_counter += 1

video.release()

cv2.destroyAllWindows()