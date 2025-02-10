import os


def publish_comics(file_name, chat_id, bot):
    file_path = os.path.join('images', file_name)
    with open(file_path, 'rb') as file:
        bot.send_photo(chat_id=chat_id, photo=file)