
import telebot
import pyowm


bot  = telebot.TeleBot('1336378712:AAH_VIxLaJmSkBmZD3WA_ptQy3bobSgz3OI')
owm = pyowm.OWM('4631328801987f3c91a7519866a729cf')
mgr = owm.weather_manager()
from pyowm.utils.config import get_default_config
config_dict = get_default_config()
config_dict['language'] = 'ru'  # your language here, eg. Portuguese
owm = pyowm.OWM('4631328801987f3c91a7519866a729cf', config_dict)

@bot.message_handler(commands=['start', 'go'])
def start_handler(message):
    bot.send_message(message.chat.id, 'Привет, милая Анечка! В каком городе ты хочешь узнать погоду? '
                                      'Если ясная, то почему бы туда не съездить? )')

@bot.message_handler(content_types=['text'])
def send_echo(message):
    observation = mgr.weather_at_place(message.text)
    w = observation.weather
    temp = w.temperature('celsius')['temp']
    answer = 'Анечка-дорогая в городе ' + message.text + ' сейчас ' + w.detailed_status + '\n'
    answer += "Температура сейчас " + str(temp) + '\n\n'

    if temp < 0:
        answer += 'на улице скользко, будь осторожней'
    elif 0 < temp < 10:
        answer += 'одевайся теплее, достаточно холодно'
    elif 10 < temp < 20:
        answer += 'на улице прохладно, но не морозно'
    else:
        answer += 'Ура, тепло!'
    bot.send_message(message.chat.id, answer)
	# bot.reply_to(message, message.text)



bot.polling(none_stop = True)



# place = input('Введите в каком городе:')
#
# print(w)
# print(w.detailed_status)
# print(w.wind())
# print('В городе ' + place + 'сейчас ' + w.detailed_status)
# print('Температура сейчас: ' + str(temp))


