import requests
from downoad_images import download_image
from telegram_bot import publish_comics
import random
import shutil
from dotenv import load_dotenv
import os
import telegram
from pathlib import Path


def parse_site_xksd(url):
    response = requests.get(url)
    response.raise_for_status() 
    latest_comic_book = response.json()
    number_latest_comic_book = latest_comic_book['num']
    random_number = random.randint(1, number_latest_comic_book)
    random_img_url = f'https://xkcd.com/{random_number}/info.0.json'
    random_img_response = requests.get(random_img_url)
    random_img_response.raise_for_status()
    comic_book = random_img_response.json()
    return comic_book


def main():
    load_dotenv()
    Path("images").mkdir(parents=True, exist_ok=True)
    chat_id = os.environ['TELEGRAM_CHAT_ID']
    bot = telegram.Bot(token=os.environ['TELEGRAM_BOT_TOKEN'])
    url = 'https://xkcd.com/info.0.json'
    comic_book = parse_site_xksd(url)
    img_url = comic_book['img']
    title_comic_book = comic_book['title']
    file_name = f'{title_comic_book}.png'
    download_image(img_url, file_name)
    publish_comics(file_name, chat_id, bot)
    shutil.rmtree('images')


if __name__ == '__main__':
    main()