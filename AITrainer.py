import cv2 as cv2
import numpy as np
import time
import PoseModule as pm
cap = cv2.VideoCapture(0)
detector = pm.poseDetector()
count = 0
count2 = 0
dir = 0
dir1 =0
pTime = 0
while True:
    success, img = cap.read()
    img = cv2.resize(img, (1080, 720))
    img = detector.findPose(img, False)
    lmList = detector.findPosition(img, False)
    # print(lmList)
    if len(lmList) != 0:
        # Right Arm
        angle = detector.findAngle(img, 12, 14, 16,False)
        per = np.interp(angle, (210, 310), (0, 100))
        bar = np.interp(angle, (220, 310), (650, 100))
        # # Left Arm
        angle2 = detector.findAngle(img, 11, 13, 15,False)
        per2 = np.interp(angle2, (210, 310), (0, 100))
        bar2 = np.interp(angle2, (220, 310), (650, 100))
        # print(angle, per)

        # Check for the dumbbell curls
        color = (255, 0, 255)
        if per == 100:
                color = (0, 255, 0)
                if dir == 0:
                        count += 0.5
                        dir = 1
        if per == 0:
            color = (0, 255, 0)
            if dir == 1:
                count += 0.5
                dir = 0
        print(count)
	#checvk for dumbell
        color2 = (255, 0, 255)
        if per2 == 100:
                color2 = (255,0,0)
                if dir1 == 0:
                        count2 += 0.5
                dir1 = 1
        if per2 == 0:
            color2 = (255,0, 0)
            if dir1 == 1:
                count2 += 0.5
                dir1 = 0
        print(count)
        print(count2)
        # Draw Bar
        #cv2.rectangle(img, (1100, 100), (1175, 650), color, 3)
        #cv2.rectangle(img, (1100, int(bar)), (1175, 650), color, cv2.FILLED)
        cv2.putText(img, f'{int(per)} %', (1100, 75), cv2.FONT_HERSHEY_PLAIN, 4,
                    color, 4)

        # Draw Curl Count
        #cv2.rectangle(img, (0, 450), (250, 720), (0, 255, 0), cv2.FILLED)
        cv2.putText(img, str(int(count)), (45, 670), cv2.FONT_HERSHEY_PLAIN, 15,
                    (0, 0, 255), 25)
	# Draw Bar2
       #cv2.rectangle(img, (100, 1100), (1175, 650), color2, 3)
        #cv2.rectangle(img, (100, int(bar2)), (650, 1175), color, cv2.FILLED)
        cv2.putText(img, f'{int(per)} %', (75, 1100), cv2.FONT_HERSHEY_PLAIN, 4,
                    color, 4)

        # Draw Curl Count2
        #cv2.rectangle(img, (0, 450), (720, 250), (0, 255, 0), cv2.FILLED)
        cv2.putText(img, str(int(count2)), (400,670), cv2.FONT_HERSHEY_PLAIN, 15,
                    (255, 0, 0), 25)

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv2.putText(img, str(int(fps)), (50, 100), cv2.FONT_HERSHEY_PLAIN, 5,
                (255, 0, 0), 5)
    #cv2.putText(img, str(int(fps)), (75, 100), cv2.FONT_HERSHEY_PLAIN, 5,
               # (255, 0, 0), 5)

    cv2.imshow("Image", img)
    cv2.waitKey(1)