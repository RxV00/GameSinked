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
title = "deneme12341234213"
#video_clip = VideoFileClip(r"C:\Users\tugra\Downloads\league_dBFjYYigr_1080_60.webm")
#audio_clip = AudioFileClip(r"C:\Users\tugra\Downloads\league_dBFjYYigr_1080_60.mp4")
#final_clip = video_clip.set_audio(audio_clip)
#final_clip.write_videofile(title + ".mp4")


os.remove(r"C:\Users\tugra\Downloads\apex_UT2EysuFc_1080_60.mp4")