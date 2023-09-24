import cv2
cam=cv2.VideoCapture(0)
cam.read()
if cam.isOpened()==False:
    print("not_connected")
while True:
    ret,img=cam.read()
    if ret==False:
        break
    cv2.imshow('t',img)
    key=cv2.waitKey(1)
    if key==27:
        break