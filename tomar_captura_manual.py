import cv2

cap = cv2.VideoCapture("aeropuerto.mp4")
contador = 0
while True:
    ret, frame = cap.read()

    cv2.imshow('video', frame)

    k = cv2.waitKey(1)

    if k == ord('h'):  # si presiono la letra h toma fotos
        contador += 1  # es igual a decir contador=contador+1
        cv2.imwrite(f"Foto{contador}.jpg", frame)

    if k == 27:
        break

cap.realese()

cv2.destroyAllWindows()
