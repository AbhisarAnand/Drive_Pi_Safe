import cv2
import numpy as np
import subprocess
import threading

CLASSES = ["background", "aeroplane", "bicycle", "bird", "boat",
           "bottle", "bus", "car", "cat", "chair", "cow", "diningtable",
           "dog", "horse", "motorbike", "person", "pottedplant", "sheep",
           "sofa", "train", "tvmonitor"]

COLORS = np.random.uniform(0, 255, size=(len(CLASSES), 3))

net = cv2.dnn.readNetFromCaffe(prototxt="models/MobileNetSSD_deploy.prototxt.txt",
                               caffeModel="models/MobileNetSSD_deploy.caffemodel")
#net.setPreferableTarget(cv2.dnn.DNN_TARGET_MYRIAD)
phone_cascade = cv2.CascadeClassifier('Phone_Cascade.xml')

audioFile = 'Alarm.wav'
personDetected = None
phoneDetected = None
v_count = 0

vs = cv2.VideoCapture(0)

def thread_for_detecting_humans():
    print("[INFO]: Starting Thread 1")
    global CLASSES
    global COLORS
    global net
    global vs
    global v_count
    global phoneDetected
    global personDetected

    while True:
        ret, frame = vs.read()
        frame2 = frame.copy()

        (h, w) = frame.shape[:2]
        blob = cv2.dnn.blobFromImage(cv2.resize(frame, (300, 300)), 0.007843, (300, 300), 127.5)

        net.setInput(blob)
        detections = net.forward()

        for i in np.arange(0, detections.shape[2]):
            confidence = detections[0, 0, i, 2]
            if confidence > 0.5:
                idx = int(detections[0, 0, i, 1])
                label = round(idx)
                # print(CLASSES[label])
                if label == 15:
                    box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
                    (startX, startY, endX, endY) = box.astype("int")
                    cv2.rectangle(frame, (startX, startY), (endX, endY), COLORS[label], 2)
                    personDetected = True

        gray = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)
        phones = phone_cascade.detectMultiScale(
            gray,
            scaleFactor=1.5,
            minNeighbors=9,
            minSize=(30, 30)
        )
        for (x, y, w, h) in phones:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 255), 2)
            font = cv2.FONT_HERSHEY_SIMPLEX
            cv2.putText(frame, 'Phone', (x - w, y - h), font, 0.5, (11, 255, 255), 2, cv2.LINE_AA)
            phoneDetected = True

        v_count += 1
        cv2.imshow("Frame", frame)
        cv2.waitKey(1)


def thread_for_playing_sound():
    print("[INFO]: Starting Thread 2")
    global phoneDetected
    global personDetected
    global audioFile
    global v_count
    averageList = []
    while True:
        if phoneDetected and personDetected:
            averageList.append(0)
            phoneDetected = False
            personDetected = False
        if len(averageList) == 3:
            subprocess.call(["aplay", audioFile])
            averageList.clear()
        if v_count % 25 == 0:
            averageList.clear()
        print(averageList)

if __name__ == "__main__":
    t1 = threading.Thread(target=thread_for_detecting_humans)
    t2 = threading.Thread(target=thread_for_playing_sound)

    t1.start()
    t2.start()
