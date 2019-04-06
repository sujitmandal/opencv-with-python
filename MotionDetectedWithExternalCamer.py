import cv2
import time
import pandas
import urllib

from datetime import datetime

first_frame = None
status_list = [None ,None]
time = []
df = pandas.DataFrame(columns = ["Start","End"])

video = cv2.VideoCapture(1)

video = cv2.VideoCapture("TCA-0 USB3.0 Camera")
video = cv2.VideoCapture("port_#0001.hub_0001")

while True:
    check, frame = video.read(0)
    status = 0

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (21, 21), 0)
    if first_frame is None:
        first_frame = gray
        continue
    
    diff_frame = cv2.absdiff(first_frame, gray)
    thresh_frame = cv2.threshold(diff_frame, 30, 255, cv2.THRESH_BINARY)[1]
    thresh_frame = cv2.dilate(thresh_frame, None, iterations = 2)

    (_, cnts, _) = cv2.findContours(thresh_frame.copy(),
                    cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in cnts:
        if cv2.contourArea(contour) < 10000:
            continue
        status = 1

        (x, y, w, h) = cv2.boundingRect(contour)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)
    status_list.append(status)

    status_list = status_list[-2:]
    if status_list[-1] == 1 and status_list[-2] == 0:
        time.append(datetime.now())
    
    if status_list[-1] == 0 and status_list[-2] == 1:
        time.append(datetime.now())

    #cv2.imshow("Gray Frame", gray)
    #cv2.imshow("Difference Frame", diff_frame)
    cv2.imshow("Threshold Frame", thresh_frame)
    cv2.imshow("Color Frame", frame)

    key = cv2.waitKey(1)
    if key == ord('e'):
        if status == 1:
            time.append(datetime.now)
        break
    
for i in range(0, len(time), 2):
    df = df.append({"Start":time[i], "End":time[i + 1]}, ignore_index = True)
df.to_csv("Time_of_Movments.csv")

video.release()
cv2.destroyAllWindows()