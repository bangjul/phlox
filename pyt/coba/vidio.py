import cv2
import numpy as np

cap = cv2.VideoCapture('video.m2ts')

indeks = 1
while(cap.isOpened()):
    ret, frame = cap.read()

    if ret is True:
        cv2.imwrite('hasil/video/tes' + str(indeks) + '.jpg', frame)
        indeks += 1
    else:
        break

cap.release()
cv2.destroyAllWindows()