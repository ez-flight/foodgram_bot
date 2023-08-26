import requests
import os
import telegram
from dotenv import load_dotenv
from PIL import Image
 
load_dotenv()

TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

bot = telegram.Bot(token=TELEGRAM_TOKEN)
# Адрес API сохраним в константе
URL = "http://188.134.84.80/api/recipes/2/"

# Сделаем GET-запрос к API
# метод json() преобразует полученный ответ JSON в тип данных, понятный Python
response = requests.get(URL).json()
homework_author = response.get("author")
food_image = response.get("image")
homework_cooking_time = response.get("cooking_time")
# Рассмотрим структуру и содержимое переменной response
print(food_image)
image = Image.open(str(food_image))
# Посмотрим, какого типа переменная response
print(type(food_image))

# response - это список. А какой длины?
print(len(response))
#bot.send_photo(TELEGRAM_CHAT_ID, photo=food_image, caption='It works!')
#bot.send_message(TELEGRAM_CHAT_ID, food_image)
image.show()

#URL = 'https://cdn2.thecatapi.com/images/3dl.jpg'


#text = 'Вам телеграмма!'
# Отправка сообщения
#bot.send_message(TELEGRAM_CHAT_ID, URL)
# Отправка изображения
#bot.send_photo(TELEGRAM_CHAT_ID, URL) 