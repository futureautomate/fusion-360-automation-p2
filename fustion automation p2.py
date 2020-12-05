# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 23:10:42 2020

@author: Tejas
"""

import pyautogui
import time 

time.sleep(2)

#while True:
#    time.sleep(1)    
#    currentMouseX, currentMouseY = pyautogui.position() # Get the XY position of the mouse.
#    print(currentMouseX, currentMouseY)

time.sleep(2)
pyautogui.moveTo(185, 114) # Move the mouse to XY coordinates.
pyautogui.click() #select sketch

time.sleep(2)
pyautogui.moveTo(903, 578) # Move the mouse to XY coordinates.
pyautogui.click() #select the plane


time.sleep(2)
pyautogui.moveTo(240, 125) # Move the mouse to XY coordinates.
pyautogui.click() #Select Rectangle

time.sleep(2)
pyautogui.moveTo(500, 500)
pyautogui.dragTo(700, 700, 1, button='left') 
pyautogui.click()



