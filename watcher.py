"""Watch my stuff.

David Smith, 2017
"""
import datetime as dt
import time
import os
import cv2

CASCADE_MODEL = 'haarcascade_frontalface_default.xml'
FACE_CASCADE = cv2.CascadeClassifier(CASCADE_MODEL)


def main(num_imgs_max=50, debug=True):
    """Watch over my desk with vigilence."""
    print('Initializing...')
    video_capture = cv2.VideoCapture(0)
    video_capture.set(3, 640)
    video_capture.set(4, 480)
    x = 0
    num_imgs = 0
    time.sleep(2)

    print('Now watching!')
    while num_imgs < num_imgs_max:
        ret, frame = video_capture.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = FACE_CASCADE.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(30, 30)
        )

        if debug:
            for (x, y, w, h) in faces:
                cv2.rectangle(gray, (x, y), (x + w, y + h), (0, 255, 0), 2)

        if len(faces) == 1:
            time.sleep(1)
            print('face found!')
            cv2.imwrite(
                os.path.join('img', str(dt.datetime.now()) + '.png'),
                gray
            )
            num_imgs += 1

        if debug:
            cv2.imshow('frame', gray)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    if debug:
        cv2.waitKey(1)
        cv2.destroyAllWindows()
        for i in range(5):
            cv2.waitKey(1)

if __name__ == '__main__':
    main(debug=True)
