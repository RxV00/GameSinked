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
from moviepy.editor import VideoFileClip, AudioFileClip, concatenate_videoclips

chrome_options = Options()
chrome_options.add_argument("--headless=new")
chrome_options.add_argument('--log-level=3')
chrome_options.add_argument('--mute-audio')
driver = webdriver.Chrome(options=chrome_options)

def baslangic():
    print(""" 
  ________                             .__        __              .___ 
 /  _____/_____    _____   ____   _____|__| ____ |  | __ ____   __| _/ 
/   \  ___\__  \  /     \_/ __ \ /  ___/  |/    \|  |/ // __ \ / __ |  
\    \_\  \/ __ \|  Y Y  \  ___/ \___ \|  |   |  \    <\  ___// /_/ |  
 \______  (____  /__|_|  /\___  >____  >__|___|  /__|_ \\___  >____ |  
        \/     \/      \/     \/     \/        \/     \/    \/     \/  
""")
    global link
    link = input("Link of the course \n")
    global game
    game = link.split('/')[4]
    automate(game)
def automate(game):
    numara = 1
    driver.get(link)
    global location
    location = finddownlaod()
    while numara <= 3:
     datalar = driver.find_elements(By.XPATH,f"/html/body/app-root/div/base-dashboard-outlet/dashboard-outlet/div/div/div[2]/div/base-dashboard-guide/dashboard-guide/div/div/div[1]/div[2]/div[2]/app-dashboard-guide-navigation/div/div[2]/ng-scrollbar/div/div/div/div/div[{numara}]/div[2]/app-dashboard-guide-navigation-item[@class = 'ng-star-inserted']")
     for data in datalar:
         time.sleep(3)
         try:
             data.click()
         except:
             driver.quit
         time.sleep(1)
         key = driver.find_element(By.XPATH,"/html/head/meta[@property='twitter:image']").get_attribute("content")
         global real_key
         real_key = key.split(game)[1][1:-1]
         hack_vid = f"https://cdn.gameleap.com/videos/{game}_{real_key}/dash/1080_60/video/{game}_{real_key}_1080_60.webm"
         hack_audio = f"https://cdn.gameleap.com/videos/{game}_{real_key}/dash/1080_60/audio/{game}_{real_key}_1080_60.mp4"
         isim = driver.current_url.split('~')[2]
         global hack_vid_isim
         hack_vid_isim = driver.find_element(By.XPATH,f"//*[@id='{isim}']/div[1]/a").get_attribute('innerText')
         global hack_vid_isimler
         hack_vid_isimler = set()
         hack_vid_isimler.add(hack_vid_isim)
         time.sleep(3)
         driver.execute_script("window.open('');")
         driver.switch_to.window (driver.window_handles[1])
         driver.get(hack_audio)
         driver.get(hack_vid)
         allah = 0
         while allah == 0:
             count = 0
             time.sleep(1)
             os.chdir(location)
             files = sorted(os.listdir(os.getcwd()),key=os.path.getmtime)
             for i in files:
                 if i.endswith(".crdownload"):
                     count = count+1
             if count == 0:
                 allah =1
                 mix_vids()
             else:
                 allah = 0
             
         driver.switch_to.window (driver.window_handles[0])
     numara += 1
    driver.quit()
    move_folder()
def finddownlaod():
    if os.name == 'nt':
        sub_key = r'SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders'
        downloads_guid = '{374DE290-123F-4565-9164-39C4925E467B}'
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, sub_key) as key:
            location = winreg.QueryValueEx(key, downloads_guid)[0]
    return location

    
def mix_vids():
    title = str(hack_vid_isim)
    try:
     video_clip = VideoFileClip(f"{location}" + f"\\{game}_{real_key}_1080_60.webm")
     audio_clip = AudioFileClip(f"{location}" + f"\\{game}_{real_key}_1080_60.mp4")
     final_clip = video_clip.set_audio(audio_clip)
     final_clip.write_videofile(title + ".mp4")
     os.remove(f"{location}" + f"\\{game}_{real_key}_1080_60.webm")
     os.remove(f"{location}" + f"\\{game}_{real_key}_1080_60.mp4")
    except:
        return (print(f"The video {title} is not available"))

def move_folder():
    sayi = 0
    isim = input("Name of the folder \n")
    os.chdir(location)
    os.makedirs(isim)
    files = sorted(os.listdir(os.getcwd()),key=os.path.getmtime)
    for file in files:
        try:
         if file in hack_vid_isimler:
              file_pathway = str(os.path.join(location,file))
              os.replace(file_pathway,os.getcwd() + "\\" + isim + "\\" + file)
              sayi += 1
        except:
            continue
    print("""
___________.__       .__       .__               .___
\_   _____/|__| ____ |__| _____|  |__   ____   __| _/
 |    __)  |  |/    \|  |/  ___/  |  \_/ __ \ / __ | 
 |     \   |  |   |  \  |\___ \|   Y  \  ___// /_/ | 
 \___  /   |__|___|  /__/____  >___|  /\___  >____ | 
     \/            \/        \/     \/     \/     \/ 
\n""")
    print(f"{sayi} Videos has been downloaded\n")
    input("Press enter to exit;")

if __name__ == '__main__':
    baslangic()
    