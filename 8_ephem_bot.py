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
import ephem_dict

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

logging.basicConfig(format ='%(name)s - %(levelname)s - %(message)s',
                    level = logging.INFO,
                    filename = 'bot.log')

def greet_user(update, context):
    text = 'Вызван /start'
    logging.info("==Command /start")
    update.message.reply_text(text)


def get_planet(update, context):
    planet_request = 'Введите одно из названий планет:\n'
    logging.info("==Command /planet")
    update.message.reply_text(planet_request+ '\n'.join(ephem_dict.planets_names))


def date_today():
    return datetime.now().strftime('%Y/%m/%d %H:%M')


def desipher_planet(user_planet):
  if user_planet.lower() in ephem_dict.planets_ephem:
    planet = ephem_dict.planets_ephem[user_planet.lower()]
  else:
    planet = None
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
