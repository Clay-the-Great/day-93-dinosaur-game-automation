from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import pyautogui
import sys
import PIL
import cv2
import time
import extcolors
# (380, 560) (470, 500)

service = Service("C:/Development/chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.get("https://elgoog.im/t-rex/")
time.sleep(1)
pyautogui.press('up')
# time.sleep(3)
# location = pyautogui.locateOnScreen("screenshots/dinosaur_head.jpg", confidence=0.7)
# print(location)
# box = pyautogui.screenshot("screenshots/box.jpg", region=(380, 500, 100, 60))

game_on = True
while game_on:
    time.sleep(0.02)
    box = pyautogui.screenshot(region=(374, 500, 100, 60))
    pixel_values = list(box.getdata())
    pixel_sum = 0
    for pixel in pixel_values:
        pixel_sum += sum(pixel)

    if pixel_sum < 4445900:
        pyautogui.press('up')


