# import the necessary packages
import numpy as np
import pyautogui
import imutils
import cv2

class gameState():
    def __init__(self):
        pass
    def takeScreenShot(self):
        pyautogui.screenshot("straight_to_disk.png")
        image = cv2.imread("straight_to_disk.png")
        cv2.imshow("Screenshot", imutils.resize(image, width=600))
        cv2.destroyAllWindows()
