import numpy as np
import cv2

vcap = cv2.VideoCapture('http://192.168.0.101:8000/stream.mjpg')

my_colors = [[158, 131, 26, 179, 255, 255], [58, 74, 0, 132, 255, 184], [0, 75, 54, 9, 253, 255]]

colors_choosed = [[255, 25, 205], [0, 201, 34], [0, 160, 255]]

points = [] #[w, y, color_id]

def find_color(img, my_colors, colors):
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    count = 0
    new_points = []
    for color in my_colors: 
        lower = np.array(color[0:3])
        upper = np.array(color[3:6])
        mask = cv2.inRange(imgHSV, lower, upper)
        x, y = get_contours(mask)
        cv2.circle(frame_final, (x, y), 10, colors[count], cv2.FILLED)
        if x != 0 and y != 0:
            new_points.append([x, y, count])
        count += 1
        #cv2.imshow(str(color[1]), mask)
    return new_points

def get_contours(img):
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    x, y, w, h = 0, 0, 0, 0
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 500:
            #cv2.drawContours(frame_final, cnt, -1, (255, 0, 0), 3)
            peri = cv2.arcLength(cnt, True)
            approx = cv2.approxPolyDP(cnt, 0.02*peri, True)
            x, y, w, h = cv2.boundingRect(approx)
    return w, y

def draw_on_canvas(points, colors):
    for point in points:
        cv2.circle(frame_final, (point[0], point[1]), 10, colors[point[2]], cv2.FILLED)


while(True):
    ret, frame = vcap.read()
    frame_final = frame.copy()
    #print cap.isOpened(), ret
    if frame is not None:
        new_points = find_color(frame, my_colors, colors_choosed)
        if len(new_points) != 0:
            for point in new_points:
                points.append(point)
        if len(points) != 0:
            draw_on_canvas(points, colors_choosed)

        cv2.imshow('frame', frame_final)
        if cv2.waitKey(22) & 0xFF == ord('q'):
            break
    else:
        print("Frame is None")
        break

vcap.release()
cv2.destroyAllWindows()
print("Video stop")