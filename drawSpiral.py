import pyautogui,time
time.sleep(5)
pyautogui.click()
distance = 600

while distance > 0:
    pyautogui.drag(distance, 0, duration=0.5)   # move right
    distance -= 20
    pyautogui.drag(0, distance, duration=0.5)   # move down
    pyautogui.drag(-distance, 0, duration=0.5)  # move left
    distance -= 20
    pyautogui.drag(0, -distance, duration=0.5)  # move up