import cv2
import numpy as np


face_cascade = cv2.CascadeClassifier(
    'cascades/data/haarcascade_frontalface_alt2.xml')

capture = cv2.VideoCapture(0)

while (True):
    # ? Capture frame-by-frame
    ret, frame = capture.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(
        gray, scaleFactor=1.5, minNeighbors=5)
    for (x, y, w, h) in faces:
        print(x, y, w, h)
        user_gray = gray[y:y+h, x:x+w]
        img_item = 'user_image.png'
        cv2.imwrite(img_item, user_gray)

        # ? Draw a rectangle around the face
        color = (51, 51, 255)  # * BGR value for the color of the rectangle
        stroke = 5  # * Defines the thickness of the lines
        end_cord_x = x + w
        end_cord_y = y + h
        cv2.rectangle(frame, (x, y), (end_cord_x, end_cord_y), color, stroke)

    # ? Display the resulting frame
    cv2.imshow('frame', frame)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

# ? When everything done, release the capture
capture.release()
cv2.destroyAllWindows()
