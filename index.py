import cv2
import pyautogui
from handtrackingmodule import handDetector
detector = handDetector(detectionCon=0.75)
cap = cv2.VideoCapture(0)
tipid = [8, 12, 16, 20]

sec = 0
sec2=0
sec3=0
tcount=3
while True:
    x, img1 = cap.read()
    img = detector.findHands(img1)
    imlist = detector.findPosition(img, draw=False)
    #print(len(imlist))
    
    if len(imlist) != 0:
        fingure_pos = []
        if imlist[4][1] > imlist[5][1]:
            fingure_pos.append(1)
        else:
            fingure_pos.append(0)
        for i in range(4):
            if imlist[tipid[i]][2] < imlist[tipid[i]-2][2]:
                fingure_pos.append(1)
            else:
                fingure_pos.append(0)
        #print(fingure_pos)
        ffingure_pos = str(fingure_pos.count(1))
        cv2.putText(img, ffingure_pos, (15, 310),
                    cv2.FONT_HERSHEY_SIMPLEX, 4, (0,0,255))
        tt=int(ffingure_pos)
        if tt==0 and fingure_pos[4]==0 and fingure_pos[0]==0:
            sec+=1
            if sec>10:
                pyautogui.press("space")
                #print("press k")
                sec=0
        if tt==2 and fingure_pos[4]==0 and fingure_pos[0]==0 and fingure_pos[1]==1:
            sec2+=1
            if sec2>8:
                pyautogui.press("up")
                #print("press up")
                sec2=0
        
        if tt==1 and fingure_pos[4]==0 and fingure_pos[3]==0 and fingure_pos[2]==0 and fingure_pos[1]==1:
            sec3+=1
            if sec3>8:
                pyautogui.press("down")
                #print("press up")
                sec3=0 
        if tt==1 and fingure_pos[4]==1 and fingure_pos[3]==0 and fingure_pos[2]==0 and fingure_pos[1]==0:
            sec3+=1
            if sec3>8:
                pyautogui.press("right")
                #print("press up")
                sec3=0
        if tt==2 and fingure_pos[4]==1 and fingure_pos[3]==0 and fingure_pos[2]==0 and fingure_pos[1]==1:
            sec3+=1
            if sec3>8:
                pyautogui.press("left")
                #print("press up")
                sec3=0
    cv2.rectangle(img, (0, 200), (150, 350), (255, 7, 55), 4)

    cv2.imshow("frm1", img)
    if cv2.waitKey(25) & 0xFF == ord("q"):
        break
cap.release()
cv2.destroyAllWindows()

