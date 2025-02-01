import os
import telegram
from dotenv import load_dotenv


def publish_comics(file_name):
    load_dotenv()
    chat_id = os.environ['TELEGRAM_CHAT_ID']
    bot = telegram.Bot(token=os.environ['TELEGRAM_BOT_TOKEN'])
    file_path = f'images/{file_name}'
    with open(file_path, 'rb') as file:
        bot.send_photo(chat_id=chat_id, photo=file)