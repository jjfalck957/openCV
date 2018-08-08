import cv2

cap = cv2.VideoCapture(0)

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH) + 0.5)
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT) + 0.5)
print('Image Width: '+ repr(width))
print('Image Height: '+repr(height))

while(True):
    ret, frame = cap.read() #What is ret?
    #rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2BGRA)
    
    
    #Drawing CrossHairs
    cv2.line(frame,(width/2,height/2-75),(width/2,height/2+75),(0,0,255),2)#cv2.line(img,(x1,y1),(x2,y2),(B,G,R),thickness)
    cv2.line(frame,(width/2-75,height/2),(width/2+75,height/2),(0,0,255),2)
    cv2.rectangle(frame,(width/2-25,height/2-25),(width/2+25,height/2+25),(0,255,0),1)
    
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        out = cv2.imwrite('capture.jpg', frame)
        break

cap.release()
cv2.destroyAllWindows()
