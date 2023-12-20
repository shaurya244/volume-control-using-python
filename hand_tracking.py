  # for id, lm in enumerate(handslms.landmark):
            #     h,w,c=frame.shape
            #     cx,cy=int(lm.x*h),int(lm.y*h)
            #     print(id,cx,cy)
                
            #     # if (id==20):
            #     #     d=[cx,cy]
            #     #     # l=l.append(d)
            #     if (id ==20):
                    
            #         cv.circle(frame,(cx,cy),20,(255,0,0),-1)
import cv2 as cv
import mediapipe as mp

cap=cv.VideoCapture(0)
mphands=mp.solutions.hands
hands=mphands.Hands()
mpdraw=mp.solutions.drawing_utils
class handdetector():
    def __init__(self,mode="flase",maxhands=2,detectioCon=0.5,trackCon=0.5):
        self.mode=mode
        self.maxhands=maxhands
        self.detectionCon=detectioCon
        self.trackCon=trackCon
        
        self.mphands=mp.solutions.hands
        self.hands=self.mphands.Hands()
        self.mpdraw=mp.solutions.drawing_utils
    def findhands (self,frame,draw="Ture"):
            

    
            
        framergb=cv.cvtColor(frame,cv.COLOR_BGR2RGB)
        results=hands.process(framergb)
    # print(results.multi_hand_landmarks)
        if results.multi_hand_landmarks:
            for handslms in results.multi_hand_landmarks:
                for id ,lms in enumerate(handslms.landmark):
                    h,w,c=frame.shape
                    cx,cy=int(lms.x*h),int(lms.y*h)
                    # d=detector.position(frame)
                    # scv.circle(frame,(cx,cy),10,(255,0,0),-1) 
                    
                if draw:
                    
                    # cv.circle(frame,(cx,cy),10,(255,0,0),-1)    
                    self.mpdraw.draw_landmarks(frame,handslms,self.mphands.HAND_CONNECTIONS)
        return frame
    def position(self,frame,handno=0,draw=True):
        d=[]
        framergb=cv.cvtColor(frame,cv.COLOR_BGR2RGB)
        results=hands.process(framergb)
        if results.multi_hand_landmarks:
            myhand=results.multi_hand_landmarks[handno]
            for id ,lms in enumerate(myhand.landmark):
                h,w,c=frame.shape
                cx,cy=int(lms.x*h),int(lms.y*w)
                d.append([id,cx,cy])
    
        return d
# while True:
    
#     istrue,frame=cap.read()
#     framergb=cv.cvtColor(frame,cv.COLOR_BGR2RGB)
#     results=hands.process(framergb)
#     # print(results.multi_hand_landmarks)
#     l=[]
#     if results.multi_hand_landmarks:
#         for handslms in results.multi_hand_landmarks:
            
#             mpdraw.draw_landmarks(frame,handslms,mphands.HAND_CONNECTIONS)
# cv.imshow("frame",frame)
# cv.waitKey(1)                
def main():
    cap=cv.VideoCapture(0)
    detector=handdetector()
    
    while True:
        isTrue,frame=cap.read()
        frame=detector.findhands(frame)
        d=detector.position(frame)
        if len(d)!=0:
            
            # print(d[4])
            cv.line(frame,(d[4][1],d[4][2]),(d[8][1],d[8][2]),(0,0,0),5)
        cv.imshow('hands',frame)
        cv.waitKey(1)
if __name__=="__main__":
    main()  
        
        
    
    