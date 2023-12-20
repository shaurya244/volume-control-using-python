import cv2 as cv
import numpy as np
import hand_tracking as ht
import math 
cap=cv.VideoCapture(0)
detector=ht.handdetector(detectioCon=0.7)
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = interface.QueryInterface(IAudioEndpointVolume)
# volume.GetMute()

vrange=volume.GetVolumeRange()
# volume.SetMasterVolumeLevel(0.0, None)
maxv=vrange[1]
minv=vrange[0]
while True:
     isTrue,frame=cap.read()
     h,w=frame.shape[0],frame.shape[1]
     frame=detector.findhands(frame)
     d=detector.position(frame)
     if len(d)!=0:
        #  print(d)
         x1,y1=d[4][1],d[4][2]
         x2,y2=d[8][1],d[8][2]
         x3,y3=(x1+x2)//2,(y1+y2)//2
         cv.circle(frame,(x1,y1),5,(255,192,203),-1)
         cv.circle(frame,(x2,y2),5,(255,192,203),-1)
         l=math.hypot(x2-x1,y2-y1)
        #  print(l)
         cv.circle(frame,(x3,y3),5,(255,192,203),-1)
         if l<50:
             cv.circle(frame,(x3,y3),15,(0,255,0),-1)
         else:
              cv.circle(frame,(x3,y3),5,(255,192,203),-1)   
         vol=np.interp(l,[5,150],[minv,maxv])
         print(vol)
         volume.SetMasterVolumeLevel(vol, None)
               
         cv.line(frame,(x1,y1),(x2,y2),(255,192,203),5)
    #  print(h,w)
     cv.imshow("frame",frame)
     cv.waitKey(1) 