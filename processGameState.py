# import the necessary packages
import numpy as np
import pyautogui
import imutils
import cv2
from settings import Settings

class gameState():
    def __init__(self):
        pass
    def takeScreenShot(self):
        print('Taking Screenshot')
        pyautogui.screenshot("screenshot.png", region=((1920/2),0, 1920, 1080))
        image = cv2.imread("screenshot.png")
        cropped = image[80:1020, 0:960]
        resized = imutils.resize(cropped, width=800)
        output = resized.copy()
        print('Converting to Gray')
        gray = cv2.cvtColor(resized, cv2.COLOR_RGB2GRAY)
        # cv2.imshow("test", gray)
        # cv2.waitKey(0)
        # detect circles in the image
        print('Detecting Circles')
        circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, minDist=1,
                           param1=50, param2=30,
                           minRadius = 8, maxRadius = 14)
        # ensure at least some circles were found
        if circles is not None:
            print('Circles Detected')
            # convert the (x, y) coordinates and radius of the circles to integers
            circles = np.round(circles[0, :]).astype("int")
        
            # loop over the (x, y) coordinates and radius of the circles
            for (x, y, r) in circles:
                # draw the circle in the output image, then draw a rectangle
               # corresponding to the center of the circle 
                red = int(output[y, x, 0])
                green = int(output[y, x, 1])
                blue = int(output[y, x, 2])
                cv2.circle(output, (x, y), r, color=(red, green, blue), thickness=4)
            myColorRed = int(output[391, 400, 0])
            myColorGreen = int(output[391, 400, 1])
            myColorBlue = int(output[391, 400, 2])
            cv2.circle(output, (391, 400), 50, color=(myColorRed, myColorGreen, myColorBlue), thickness=5)
            # show the output image
            cv2.imshow("output", output)
            # cv2.imshow("output", np.hstack([image, output]))
            cv2.waitKey(0)
        else:
            print('na')
        # cv2.imshow("Screenshot", imutils.resize(gray, width=600))
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()
