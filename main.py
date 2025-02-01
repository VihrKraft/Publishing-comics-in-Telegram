import requests
from downoad_images import download_image
from telegram_bot import publish_comics
import random
import shutil


def main():
    url = 'https://xkcd.com/info.0.json'
    response = requests.get(url)
    response.raise_for_status() 
    latest_comic_book = response.json()
    number_latest_comic_book = latest_comic_book['num']
    random_number = random.randint(1, number_latest_comic_book)
    random_img_url = f'https://xkcd.com/{random_number}/info.0.json'
    random_img_response = requests.get(random_img_url)
    random_img_response.raise_for_status()
    comic_book = random_img_response.json()
    img_url = comic_book['img']
    title_comic_book = comic_book['title']
    file_name = f'{title_comic_book}.png'
    download_image(img_url, file_name)
    publish_comics(file_name)
    shutil.rmtree('images')


if __name__ == '__main__':
    main()