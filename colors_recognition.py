import numpy as np
import cv2

vcap = cv2.VideoCapture('http://192.168.0.101:8000/stream.mjpg')

#def find_color(img):
#    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
#    lower = np.array([h_min, s_min, v_min])
#    upper = np.array([h_max, s_max, v_max])
#    mask = cv2.inRange(imgHSV, lower, upper)
#    cv2.imshow("img", mask)

while(True):
    ret, frame = vcap.read()
    #print cap.isOpened(), ret
    if frame is not None:
        cv2.imshow('frame',frame)
        if cv2.waitKey(22) & 0xFF == ord('q'):
            break
    else:
        print("Frame is None")
        break

vcap.release()
cv2.destroyAllWindows()
print("Video stop")