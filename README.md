# Twitch-Video-Stats-Analyzer

This program is for analyzing Twitch video stats for 1 minutes by capturing the screen and extracting text from the picture.
To calculate average FPS, bitrate, and latency, you need to modify some codes like below:

-Set the location to save the captured photos.
screenshot_folder = '/User/Example/'
-Set the location to save output.txt file.
f= open("/Users/Example/output.txt","w+") # modify before '/output.txt'
-set the screen area you want to capture.
screenshot = pyautogui.screenshot(screenshot_name, region=(left, top, right, bottom)) 
