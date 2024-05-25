from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import os
import time
from pathlib import Path
import winreg

if os.name == 'nt':
    sub_key = r'SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders'
    downloads_guid = '{374DE290-123F-4565-9164-39C4925E467B}'
    with winreg.OpenKey(winreg.HKEY_CURRENT_USER, sub_key) as key:
        location = winreg.QueryValueEx(key, downloads_guid)[0]

hack_vid_isimler = {"Mastering Your First Clear.mp4","Top 5 Tips and Tricks.mp4","A Crash Course.mp4"}

isim = input("Name of the folder \n")
os.chdir(location)
os.makedirs(isim)
files = sorted(os.listdir(os.getcwd()),key=os.path.getmtime)
print(files)
for file in files:
    try:
        if str(file) in hack_vid_isimler:
            print(file)
            file_pathway = str(os.path.join(location,file))
            print(file_pathway)
            print(os.getcwd() + "\\" + isim + "\\" + file)
            os.replace(file_pathway,os.getcwd() + "\\" + isim + "\\" + file)
    except:
         continue

    
