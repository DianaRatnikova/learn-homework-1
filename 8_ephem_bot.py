"""
Домашнее задание №1

Использование библиотек: ephem

* Установите модуль ephem  ( сделано: pip install ephem)
* Добавьте в бота команду /planet, которая будет принимать на вход
  название планеты на английском, например /planet Mars
* В функции-обработчике команды из update.message.text получите
  название планеты (подсказка: используйте .split())
* При помощи условного оператора if и ephem.constellation научите
  бота отвечать, в каком созвездии сегодня находится планета.

"""

from datetime import datetime
import logging
import settings
import ephem

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

logging.basicConfig(format ='%(name)s - %(levelname)s - %(message)s',
                    level = logging.INFO,
                    filename = 'bot.log')


PROXY = {
    'proxy_url': 'socks5://t1.learn.python.ru:1080',
    'urllib3_proxy_kwargs': {
        'username': 'learn',
        'password': 'python'
    }
}

planets_names = ['Sun', 'Moon', 'Mercury', 'Venus', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune', 'Pluto']

def greet_user(update, context):
    text = 'Вызван /start'
    print(text)
    update.message.reply_text(text)


def get_planet(update, context):
    planet_request = 'Введите одно из названий планет:'
    print(planet_request)
    for planet_variant in planets_names:
      planet_request +='\n' + planet_variant
    update.message.reply_text(planet_request)


def date_today():
    dt_now = datetime.now()
    dt_for_constellation = dt_now.strftime('%Y/%m/%d %H:%M')
    return dt_for_constellation


def desipher_planet(user_planet):
  if user_planet.lower() == 'sun':
    planet = ephem.Sun()
  elif user_planet.lower() == 'moon':
    planet = ephem.Moon()
  elif user_planet.lower() == 'mercury':
    planet = ephem.Mercury()
  elif user_planet.lower() == 'venus':
    planet = ephem.Venus()    
  elif user_planet.lower() == 'mars':
    planet = ephem.Mars()
  elif user_planet.lower() == 'jupiter':
    planet = ephem.Jupiter()
  elif user_planet.lower() == 'saturn':
    planet = ephem.Saturn()
  elif user_planet.lower() == 'uranus':
    planet = ephem.Uranus()
  elif user_planet.lower() == 'neptune':
    planet = ephem.Neptune()
  elif user_planet.lower() == 'pluto':
    planet = ephem.Pluto()
  else:
    planet=None
  return planet


def talk_to_me(update, context):
    user_planet = update.message.text
    planet = desipher_planet(user_planet)
    if planet:
       planet.compute(date_today())
       constellation =  ephem.constellation(planet)
       message_for_user = f"Планета {user_planet} находится в созвездии {constellation} на дату {date_today()}"
       update.message.reply_text(message_for_user)
    else:
      update.message.reply_text('нет такой планеты')



def main():
    mybot = Updater(settings.API_KEY, use_context=True)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", get_planet))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    logging.info("Бот стартовал / Bot started")

    mybot.start_polling()
    mybot.idle()

if __name__ == "__main__":
    main()
