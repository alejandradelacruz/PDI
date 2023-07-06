"""
Created on Mon July 07 
@autor: Alejandra De la cruz De la cruz 
"""

import numpy as np
import cv2

cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cv2.namedWindow("seguimiento", cv2.WINDOW_NORMAL)
tracker = cv2.TrackerCSRT_create()
conteo = 0
while True:
    res, frame = cam.read()
    if conteo == 10:
        r = cv2.selectROI("seguimiento", frame)
        tracker.init(frame, r)
        
    try:
        trackRealizado, r = tracker.update(frame)
        if trackRealizado:
            supIzq = (int(r[0]), int(r[1]))
            infDer = (int(r[0] + r[2]), int(r[1] + r[3]))
            cv2.rectangle(frame, supIzq, infDer, (0,255,0), 2)
            cv2.putText(frame, "Objeto detectado", supIzq, cv2.FONT_HERSHEY_SIMPLEX, 1.0,
                        (0,0,255), 2) 
    except:
        pass
    
    conteo += 1
    cv2.imshow("seguimiento", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
cam.release()
cv2.destroyAllWindows()