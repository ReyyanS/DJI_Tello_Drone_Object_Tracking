from djitellopy import Tello
from playsound import playsound
import cv2
import time

def initializeTello():
    myDrone = Tello()
    myDrone.connect()
    myDrone.for_back_velocity = 0
    myDrone.left_right_velocity = 0
    myDrone.up_down_velocity =100
    myDrone.yaw_velocity =0
    myDrone.speed = 0
    print(myDrone.get_battery())
    myDrone.streamoff()
    myDrone.streamon()
    return myDrone

def telloGetFrame(myDrone, w=360,h=240):
    myFrame = myDrone.get_frame_read()
    myFrame = myFrame.frame
    img = cv2.resize(myFrame,(w,h))
    return img

def findFaultyRail(img):
    objCascade = cv2.CascadeClassifier('faultyrail.xml')
    imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    objects = objCascade.detectMultiScale(imgGray,1.2,4)

    for(x,y,w,h) in objects:
        cv2.rectangle(img,(x,y), (x+w,y+h),(0,0,255),2)
        playsound("beep.mp3")

    return img

def findCar(img):
    objCascade = cv2.CascadeClassifier('car.xml')
    imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    objects = objCascade.detectMultiScale(imgGray,1.2,4)

    for(x,y,w,h) in objects:
        cv2.rectangle(img,(x,y), (x+w,y+h),(255,0,0),2)
        playsound("beep.mp3")
    return img

def findWood(img):
    objCascade = cv2.CascadeClassifier('wood.xml')
    imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    objects = objCascade.detectMultiScale(imgGray,1.2,4)

    for(x,y,w,h) in objects:
        cv2.rectangle(img,(x,y), (x+w,y+h),(0,255,0),2)
        playsound("beep.mp3")
    return img
