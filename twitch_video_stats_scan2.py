import time
import pyautogui
from PIL import Image
from pytesseract import *
import numpy as np

# This program is for analyzing Twitch video stats for 1 minutes 
# by capturing the screen and extracting text from the picture.
# To calculate average FPS, bitrate, and latency, you need to modify some codes

# please modify this part
# Set the location to save the captured photos.
screenshot_folder = '/User/Example/'
# Set the location to save output.txt file.
f= open("/Users/Example/output.txt","w+") # modify before '/output.txt'

# Expected server allocation for each location. 
#CA : US seattle
#AUS : US Los Angeles
#KOR : KOR Seoul
#UK : UK London
#US : Unkown

num_screenshot = 1
fps = []
latency_to_broadcaster = []
playback_bitrate = []
# Take a screenshot every second for 1 minute
for i in range(60):
    f.write(f"Screenshot {num_screenshot}\n")
    screenshot_name = f'{screenshot_folder}Screenshot_{time.strftime("%Y%m%d_%H%M%S")}.png'
    # please modify this part region=(left, top, right, bottom)
    # This sets the screen area you want to capture.
    screenshot = pyautogui.screenshot(screenshot_name, region=(60, 315, 365, 500)) 
    screenshot.save(screenshot_name)
    count = 0
    do = False
    stop = False
    img = np.array(Image.open(screenshot_name))
    text = pytesseract.image_to_string(img)
    words = text.split()
    for text in words:
        if do:
            f.write(f'{text}\n')
            do = False
            if count == 1:
                try:
                    fps.append(int(text))
                except ValueError:
                    print('Invalid value: skip this screenshot')
                    break
            elif count == 2:
                try:
                    latency_to_broadcaster.append(float(text))
                except ValueError:
                    print('Invalid value: skip this screenshot')
                    break
            elif count == 3:
                try:
                    playback_bitrate.append(int(text))
                except ValueError:
                    print('Invalid value: skip this screenshot')
                    break
            if stop:
                break
            continue
        if text == "FPS":
            f.write("FPS: ")
            do = True
            count += 1
        if text == "Broadcaster":
            f.write("Latency To Broadcaster: ")
            do = True
            count += 1
        if text == "Bitrate":
            f.write("Playback Bitrate: ")
            do = True
            count += 1
            stop = True

    
    f.write("\n")
    print(f"Screenshot {num_screenshot} is done")
    num_screenshot += 1
    # 1 second interval
    time.sleep(1)

f.write(f'Average of fps : {(sum(fps)/len(fps)): .2f}\n')
f.write(f'Average of latency to broadcaster : {(sum(latency_to_broadcaster)/len(latency_to_broadcaster)): .2f} sec.\n')
f.write(f'Average of playback bitrate : {(sum(playback_bitrate)/len(playback_bitrate)): .2f} Kbps\n')
f.write("Video stats analysis is done.")
f.close
print("Video stats analysis is done.")