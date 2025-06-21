import pyautogui
x, y, width, height = 0, 0, 192, 180
region = (x, y, width, height)
# Take a screenshot of the specified region
myScreen = pyautogui.screenshot(region=region)
# Save the screenshot to a file
myScreen.save("C:/Users/Mohit/Downloads/screenshott.png")

