import telebot
import random
from telebot import types
bot = telebot.TeleBot("")

global flag
flag = 1

@bot.message_handler(commands=['off'])
def off(m):
 global flag
 if flag == 1:
  flag = 0
  #k = types.ReplyKeyboardRemove(selective=False)
  #bot.reply_to(m, 'Ваша подписка деактивирована.' + '\n', reply_markup=k)
  mk = types.ReplyKeyboardMarkup(resize_keyboard=True)
  end_button = types.KeyboardButton('Включить бота')
  mk.add(end_button)
  bot.send_message(m.chat.id,'Ваша подписка деактивирована.' + '\n' + 'Вы всегда можете включить ее снова с помощью команды /on.', reply_markup=mk)

@bot.message_handler(commands=['on'])
def on(m):
 global flag
 if flag == 0:
    flag = 1
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buy_button = types.KeyboardButton('Купить сейчас')
    info_button = types.KeyboardButton('Информация')
    price_button = types.KeyboardButton('Цены')
    rules_button = types.KeyboardButton('Правила')
    job_button = types.KeyboardButton('Работа')
    cont_button = types.KeyboardButton('Контакты')
    markup.add(buy_button)
    markup.add(info_button, price_button)
    markup.add(rules_button)
    markup.add(job_button, cont_button)
    bot.send_message(m.chat.id, text='Бот снова активирован!',reply_markup=markup)

@bot.message_handler(regexp='^Включить бота')
def on(m):
 global flag
 if flag == 0:
   flag = 1
   markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
   buy_button = types.KeyboardButton('Купить сейчас')
   info_button = types.KeyboardButton('Информация')
   price_button = types.KeyboardButton('Цены')
   rules_button = types.KeyboardButton('Правила')
   job_button = types.KeyboardButton('Работа')
   cont_button = types.KeyboardButton('Контакты')
   markup.add(buy_button)
   markup.add(info_button, price_button)
   markup.add(rules_button)
   markup.add(job_button, cont_button)
   bot.send_message(m.chat.id, text='Бот снова активирован!',reply_markup=markup)
 
@bot.message_handler(commands=['start'])
def start(m):
   markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
   buy_button = types.KeyboardButton('Купить сейчас')
   info_button = types.KeyboardButton('Информация')
   price_button = types.KeyboardButton('Цены')
   rules_button = types.KeyboardButton('Правила')
   job_button = types.KeyboardButton('Работа')
   cont_button = types.KeyboardButton('Контакты')
   markup.add(buy_button)
   markup.add(info_button, price_button)
   markup.add(rules_button)
   markup.add(job_button, cont_button)
   bot.send_message(m.chat.id, text='Приветствуем вас, дорогой гость!' + '\n\n' + 'Чтобы приостановить подписку, нажмите /off.',reply_markup=markup)

@bot.message_handler(commands=['buy'])
def buy(m):
   bot.send_message(m.chat.id,'✅Заказ принят!')

@bot.message_handler(commands=['check'])
def check(m):
   bot.send_message(m.chat.id,'Статус заказа: ⛔️НЕ ОПЛАЧЕН.')
  
@bot.message_handler(regexp='^Информация')
def mosy(m):
   bot.send_message(m.chat.id,'Ответы на часто задаваемые вопросы:')
  
@bot.message_handler(regexp='^Цены')
def mosy(m):
   bot.send_message(m.chat.id,'📖 ПРАЙС–ЛИСТ [Москва]')
  
@bot.message_handler(regexp='^Правила')
def mosy(m):
   bot.send_message(m.chat.id, 'ПРАВИЛА🧷')

@bot.message_handler(regexp='^Работа')
def mosy(m):
   bot.send_message(m.chat.id,'Приемлемый график, хорошая заработная плата, премии, бонусы...')

@bot.message_handler(regexp='^Контакты')
def mosy(m):
   bot.send_message(m.chat.id,'Контакты❗')

@bot.message_handler(regexp='^Купить сейчас')
def buy(m):
   markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
   dist1 = types.KeyboardButton('ЦАО (Басманный, Красносельский, Хамовники)')
   dist2 = types.KeyboardButton('САО (Аэропорт, Беговой)')
   dist3 = types.KeyboardButton('СВАО (Альтуфьевский, Отрадное, Свиблово)')
   dist4 = types.KeyboardButton('ВАО (Измайлово, Северное Измайлово)')
   dist5 = types.KeyboardButton('ЮВАО (Печатники)')
   dist6 = types.KeyboardButton('ЮАО (Чертаново Центральное, Чертаново Южное)')
   dist7 = types.KeyboardButton('ЗАО (Кунцево)')
   dist8 = types.KeyboardButton('СЗАО (Митино, Строгино)')
   back = types.KeyboardButton('Назад')
   markup.add(dist1)
   markup.add(dist2)
   markup.add(dist3)
   markup.add(dist4)
   markup.add(dist5)
   markup.add(dist6)
   markup.add(dist7)
   markup.add(dist8)
   markup.add(back)
   bot.send_message(m.chat.id, text='Выберите район',reply_markup=markup)
  
@bot.message_handler(regexp='^Назад')
def back(m):
  markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
  buy_button = types.KeyboardButton('Купить сейчас')
  info_button = types.KeyboardButton('Информация')
  price_button = types.KeyboardButton('Цены')
  rules_button = types.KeyboardButton('Правила')
  job_button = types.KeyboardButton('Работа')
  cont_button = types.KeyboardButton('Контакты')
  markup.add(buy_button)
  markup.add(info_button, price_button)
  markup.add(rules_button)
  markup.add(job_button, cont_button)
  bot.send_message(m.chat.id, text='Главное меню',reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == "ЦАО (Басманный, Красносельский, Хамовники)")
def mosy(m):
  bot.send_message(m.chat.id,'📖 ПРАЙС–ЛИСТ [ЦАО]')

@bot.message_handler(func=lambda message: message.text == "САО (Аэропорт, Беговой)")
def mosy(m):
  bot.send_message(m.chat.id,'📖 ПРАЙС–ЛИСТ [САО]')
  
@bot.message_handler(func=lambda message: message.text == "СВАО (Альтуфьевский, Отрадное, Свиблово)")
def mosy(m):
  bot.send_message(m.chat.id,'📖 ПРАЙС–ЛИСТ [СВАО]')

@bot.message_handler(func=lambda message: message.text == "ВАО (Измайлово, Северное Измайлово)")
def mosy(m):
  bot.send_message(m.chat.id,'📖 ПРАЙС–ЛИСТ [ВАО]')

@bot.message_handler(func=lambda message: message.text == "ЮВАО (Печатники)")
def mosy(m):
  bot.send_message(m.chat.id,'📖 ПРАЙС–ЛИСТ [ЮВАО]')

@bot.message_handler(func=lambda message: message.text == "ЮАО (Чертаново Центральное, Чертаново Южное)")
def mosy(m):
  bot.send_message(m.chat.id,'📖 ПРАЙС–ЛИСТ [ЮАО]')
  
@bot.message_handler(func=lambda message: message.text == "ЗАО (Кунцево)")
def mosy(m):
  bot.send_message(m.chat.id,'📖 ПРАЙС–ЛИСТ [ЗАО]')
  
@bot.message_handler(func=lambda message: message.text == "СЗАО (Митино, Строгино)")
def mosy(m):
  bot.send_message(m.chat.id,'📖 ПРАЙС–ЛИСТ [СЗАО]') 

bot.polling(True)
