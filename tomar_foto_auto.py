import cv2

import time

cap = cv2.VideoCapture(0)
c = 0
while True:
    ret, frame = cap.read()

    cv2.imshow("video", frame)

    c += 1

    if c <= 6:
        cv2.imwrite(f"Foto{c}.jpg", frame)
        time.sleep(0.06)
    else:
        break
cap.release()
cv2.destroyAllWindows()
