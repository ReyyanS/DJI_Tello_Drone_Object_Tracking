from utlis import *
import cv2
import time

w,h= 1280,720

fly=1

myDrone = initializeTello()


while True:
    ##Step1
    img = telloGetFrame(myDrone, w, h)
    ##Step2

    img = findFaultyRail(img)
    img2 = findWood(img)
    img3 = findCar(img)
    cv2.imshow('Image', img)

    if fly == 2:
        myDrone.takeoff()
        myDrone.land()
        fly = 2

    if cv2.waitKey(1) and 0x0FF == ord('q'):
        myDrone.land()
        break
