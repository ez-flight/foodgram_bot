import requests  # Импортируем библиотеку для работы с запросами
import os

from telegram import Bot
from dotenv import load_dotenv

load_dotenv()

token = os.getenv('TOKEN')
CHAT_ID = '790509402'  # Укажите chat_id

bot = Bot(token=token)
# Адрес API сохраним в константе
URL = "http://188.134.84.80/api/recipes/2/"

# Сделаем GET-запрос к API
# метод json() преобразует полученный ответ JSON в тип данных, понятный Python
response = requests.get(URL).json()

# Рассмотрим структуру и содержимое переменной response
print(response)

# Посмотрим, какого типа переменная response
print(type(response))

# response - это список. А какой длины?
print(len(response))
