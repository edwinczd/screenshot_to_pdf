from PIL import Image, ImageGrab
import pyautogui
import time

page_count = #Number of pages
cover_location = "Cover.png"  #Name of the cover picture

# IMPORTANT: Specify the dimension of your screenshot.
# X1, Y1 is the top left corner
# X2, Y2 is the bottom right corner
# Use pyautogui.position() to find out the coordinates
X1 = 
Y1 = 
X2 = 
Y2 = 

time.sleep(5)  #Time to switch screen

screen_size = (X1, Y1, X2, Y2)
list = []
cover = Image.open(cover_location).convert("RGB")

for i in range(0, page_count):
    pyautogui.click() #Click to go to the next page, can adjust to other button or manually perform the action
    time.sleep(0.5) #Delay between screenshots, can adjust if necessary 
    im = ImageGrab.grab(bbox=screen_size).convert('RGB')
    list.append(im)

cover.save("Book.pdf", "PDF", resolution=100.0, save_all=True, append_images=im_list)
