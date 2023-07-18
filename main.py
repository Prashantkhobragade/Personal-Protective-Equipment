from ultralytics import YOLO
import cv2
import cvzone
import math

#webcam
#cap = cv2.VideoCapture(0)
#cap.set(3,720)
#cap.set(4,360)

#video
cap = cv2.VideoCapture('Videos/ppe-2.mp4')

model = YOLO("ppe.pt")

classNames = ['Hardhat', 'Mask', 'NO-Hardhat', 'NO-Mask', 'NO-Safety Vest', 'Person', 'Safety Cone',
              'Safety Vest', 'machinery', 'vehicle']


              
MyColor = (0,0,255)
while True:
    success, img = cap.read()
    results = model(img, stream=True)

    for r in results:
        boxes = r.boxes
        for box in boxes:
            #bonding box
            x1, y1, x2, y2 = box.xyxy[0]
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
            w, h = x2-x1, y2-y1
            #cvzone.cornerRect(img, (x1, y1, w, h))
            #cv.rectangle(img, (x1,y1),(x2,y2), MyColor,3)

            #confidance
            conf = math.ceil((box.conf[0]*100))/100

            #className
            cls = int(box.cls[0])

            currentclass = classNames[cls]
            if conf > 0.5:
                if currentclass == "Hardhat" or currentclass == "Mask" or currentclass == "Safety Vest":
                    MyColor = (0,255,0)
                elif currentclass == "NO-Hardhat" or currentclass == "NO-Mask" or currentclass == "NO-Safety Vest":
                    MyColor = (0,0,255)
                else:
                    MyColor = (255,0,0)

                cvzone.putTextRect(img, f'{classNames[cls]} {conf}', (max(0, x1), 
                max(35, y1)), scale=1, thickness=1,colorB=MyColor, colorR=MyColor,
                colorT=(255,255,255),
                offset=5)

                cv2.rectangle(img, (x1,y1),(x2,y2), MyColor,3)


    
    
    cv2.imshow("image", img)
    cv2.waitKey(1)
