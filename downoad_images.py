from pathlib import Path
import requests
import os


def download_image(url, file_name):
    Path("images").mkdir(parents=True, exist_ok=True)
    file_path = os.path.join('images', file_name)  
    response = requests.get(url)
    response.raise_for_status()
    with open(file_path, 'wb') as file:
        file.write(response.content)