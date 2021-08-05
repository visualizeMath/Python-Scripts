import pyautogui
import time

time.sleep(5)
# pyautogui.click('firca.png')
# pyautogui.moveRel(200,200,duration=0.2)
pyautogui.click()
distance=400 
pyautogui.dragRel(distance,0,duration=0.2) #move right
uprightX,uprightY=pyautogui.position()
pyautogui.dragRel(0,distance,duration=0.2) #move down
downrightX,downrightY=pyautogui.position()
pyautogui.dragRel(-distance,0,duration=0.2) #move left
downleftX,downleftY=pyautogui.position()
pyautogui.dragRel(0,-distance,duration=0.2) #move up
upleftX,upleftY=pyautogui.position()
# print('upleftX :',upleftX,'upleftY:',upleftY)
distance=400
pyautogui.moveRel(distance/2,distance/2, duration=0.25)
upleftX2,upleftY2=pyautogui.position()
# print('upleftX2:',upleftX2,'upleftY2:',upleftY2)
pyautogui.dragRel(distance,0, duration=0.25) #move right
uprightX2,uprightY2=pyautogui.position()
pyautogui.dragRel(0,distance,duration=0.2) #move down
downrightX2,downrightY2=pyautogui.position() # get the position of pointer 
pyautogui.dragRel(-distance,0,duration=0.2) #move left
downleftX2,downleftY2=pyautogui.position()
pyautogui.dragRel(0,-distance,duration=0.2) #move up

#move the pointer from upper left corner of the second square to upper left corner of the first square
pyautogui.moveTo(upleftX2,upleftY2)
pyautogui.click()
#connect upper left corners
pyautogui.drag(-(upleftX2-upleftX),-(upleftY2-upleftY),duration=0.2)
#connect upper right corners
pyautogui.moveTo(uprightX2,uprightY2)
pyautogui.click()
pyautogui.drag(-(uprightX2-uprightX),-(uprightY2-uprightY),duration=0.2)

#connect lower right corners
pyautogui.moveTo(downrightX2,downrightY2)
pyautogui.click()
pyautogui.drag(-(downrightX2-downrightX),-(downrightY2-downrightY),duration=0.2)

#connect lower left corners
pyautogui.moveTo(downleftX2,downleftY2)
pyautogui.click()
pyautogui.drag(-(downleftX2-downleftX),-(downleftY2-downleftY),duration=0.2)