import pyautogui
myscreen = pyautogui.screenshot()
myscreen.save("C:/Users/Mohit/Downloads/screenshot.png")
# This code takes a screenshot of the current screen and saves it as "screenshot.png"
# Note: Make sure you have the pyautogui library installed in your Python environment.
# You can install it using pip if you haven't already:
# pip install pyautogui
# Ensure that the script has permission to take screenshots, as some systems may require additional permissions.
# You can also specify a different file path if you want to save the screenshot in a specific directory.
# Example: myscreen.save("/path/to/directory/screenshot.png")
# If you want to take a screenshot of a specific region, you can use the region parameter:
