from bs4 import BeautifulSoup
import requests
import os
import time
from dotenv import load_dotenv
import urllib.request

load_dotenv()

host = os.environ["70MAI_IP"];
ext = os.environ[EXTENSION]

# Here u can put all folders to sync.
camDirs = ["/sd/Normal/Front/"]

def listFD(url, ext=''):
  page = requests.get(url).text
  soup = BeautifulSoup(page, 'html.parser')
  return [node.get('href') for node in soup.find_all('a') if node.get('href').endswith(ext)]

while True:
  try:
    print("Searching host...")
    for dir in camDirs:
      files = listFD(host + dir, ext)
      for file in files:
        nameFile = file.rsplit('/', 1)
        print("Downloading file..." + nameFile )
        if not os.path.isfile(nameFile):
          urllib.request.urlretrieve(host + dir + '/' + nameFile, file)
        if len(files) > 0:
          print("Trabajo completado")
          time.sleep(6000)
  except:
    print("host not found")
  finally:
    # Wait 60s to retry
    time.sleep(60)
    