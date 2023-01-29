import cv2 as cv
import numpy as np

videoCapture = cv.VideoCapture(0)
preCircle = None
dist = lambda x1, y1, x2, y2: (x1-x2)**2+(y1-y2)**2

while True:
    ret, frame = videoCapture.read()

    if not ret:
        break

    grayFrame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    blurFrame = cv.GaussianBlur(grayFrame, (17, 17), 0)

    circles = cv.HoughCircles(blurFrame, cv.HOUGH_GRADIENT, 1.2, 100,
                             param1=100, param2=30, minRadius=75, maxRadius=400)

    if circles is not None:
        circles = np.uint16(np.around(circles))
        chosen = None

        for i in circles[0, :]:
            if chosen is None:
                chosen = i
            if preCircle is not None:
                if dist(chosen[0], chosen[1], preCircle[0], preCircle[1]) <= dist(i[0], i[1], preCircle[0], preCircle[1]):
                    chosen = i
        cv.circle(frame, (chosen[0], chosen[1]), 1, (0, 100, 100), 3)
        cv.circle(frame, (chosen[0], chosen[1]), chosen[2], (255, 0, 255), 3)
        preCircle = chosen

    cv.imshow("circles", frame)

    if cv.waitKey(1) & 0xFF == ord('q'):
        break


videoCapture.release()
cv.destroyAllWindows()