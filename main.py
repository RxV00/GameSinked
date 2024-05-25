from urllib import request
import threading
import requests
import os
from tqdm import tqdm
#/html/head/meta[10] bunu yapistirdiktan sonra cikan elemanin contentini al ordan id yi ayikla sonra ZcydGVoRr yerine koy
#title xpath //*[@id="vguide_Rp_1g-ePz"]/div[1]/a
#diger oyunlar icin valorant yerine sadece obur oyunun i https://cdn.gameleap.com/videos/valorant_ZcydGVoRr/dash/1080_60/video/valorant_ZcydGVoRr_1080_60.webm msmi gelecek
video_url = "https://cdn.gameleap.com/videos/valorant_ZcydGVoRr/dash/1080_60/video/valorant_ZcydGVoRr_1080_60.webm"
audio_url = "https://cdn.gameleap.com/videos/valorant_ZcydGVoRr/dash/1080_60/audio/valorant_ZcydGVoRr_1080_60.mp4"

# Modify Here
video_id = ["GL7Km68N_", "VXhl2mD0_", ]

video_name = ["8-How to Attack like a Pro Raze", "17-How to Dominate Haven as Raze"]
# Modify Here


class DownloadThread(threading.Thread):
    def __init__(self, url, name):
        threading.Thread.__init__(self)
        self.name = name
        self.url = url
        self.status = None

    def run(self):
        download_folder = "downloads"
        if not os.path.exists(download_folder):
            os.makedirs(download_folder)
        file_path = os.path.join(download_folder, self.name)
        self.status = "downloading"
        file_size = 0
        if os.path.exists(file_path):
            file_size = os.path.getsize(file_path)
        
        headers = {"Range": "bytes={}-".format(file_size)}
        response = requests.get(self.url, headers=headers, stream=True)
        
        total_size = int(response.headers.get('content-length', 0)) + file_size
        block_size = 1024
        t = tqdm(total=total_size, unit='B', unit_scale=True, desc=self.name,
                 bar_format='{l_bar}{bar}| {n_fmt}/{total_fmt}')
        with open(file_path, "ab") as f:
            for data in response.iter_content(block_size):
                if self.status == "paused":
                    self.status = "paused"
                    while self.status == "paused":
                        pass
                t.update(len(data))
                f.write(data)
        t.close()
        self.status = "done"

class MultiThreadDownloader:
    def __init__(self):
        self.threads = []
    
    def download(self, url_list, file_name, file_type):
        for i, url in enumerate(url_list):
            name = "{}.{}".format(file_name[i], file_type)
            thread = DownloadThread(url, name)
            self.threads.append(thread)
            thread.start()
    
    def pause(self):
        for thread in self.threads:
            if thread.status == "downloading":
                thread.status = "paused"
    
    def resume(self):
        for thread in self.threads:
            if thread.status == "paused":
                thread.status = "downloading"

if __name__ == "__main__":
    videoUrls = []
    audioUrls = []

    for i in range(0, len(video_id)):
        v_url = video_url
        a_url = audio_url

        v_url = v_url.replace("ZcydGVoRr", video_id[i])
        a_url = a_url.replace("ZcydGVoRr", video_id[i])
        print(v_url)

        videoUrls.append(v_url)
        audioUrls.append(a_url)

    downloader = MultiThreadDownloader()
    downloader.download(videoUrls, video_name, "webm")
    downloader.download(audioUrls, video_name, "mp4")