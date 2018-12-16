import random
import requests
import vk_api
from config import *

def write_msg(user_id, text):
  vk_bot.method('messages.send', {'user_id': user_id, 'message': text, 'random_id': random.randint(0, 10000)})
def write_msg_attach(user_id, text, att_url):
  vk_bot.method('messages.send',
             {'user_id': user_id,
             'attachment': att_url,
             'message': text,
             'random_id': random.randint(0, 100000)})



vk_bot = vk_api.VkApi(token=TOKEN)
long_poll = vk_bot.method('messages.getLongPollServer', {'need_pts': 1, 'lp_version': 3})
server, key, ts = long_poll['server'], long_poll['key'], long_poll['ts']
print("готов к использованию")
# + str(long_poll))

while True:
 long_poll = requests.get('https://{server}?act={act}&key={key}&ts={ts}&wait=5000000000000'.format(server=server,
                                                                                        act='a_check',
                                                                                        key=key,
                                                                                        ts=ts)).json()
 update = long_poll['updates']
 if update[0][0] == 4:
 #print(update)
  user_id = update[0][3]
  user_name = vk_bot.method('users.get', {'user_ids': user_id})
  print(str(user_name[0]['first_name']) + ' ' + str(user_name[0]['last_name']) + ' написал(а) боту - ' + str(update[0][6]))
  if '650' in update[0][6]:
     write_msg_attach(user_id,
                      'Затычка',
                      'photo261166398_456239824')
  if '660ti' in update[0][6]:
     write_msg_attach(user_id,
                      'Лучше 750ти на 2-3 фпс, особенно в 1920х1080',
                      'photo261166398_456239827')
  if 'муз' in update[0][6]:
     write_msg_attach(user_id,
                      'слушай',
                      'audio261166398_456239173')
  if '660' in update[0][6]:
      write_msg_attach(user_id,
                       'Как 750ти, но шина шире',
                       'photo261166398_456239833')
  if '650ti' in update[0][6]:
      write_msg_attach(user_id,
                           'Затычка, если повезет найдешь версию на 2 гига',
                           'photo261166398_456239826')
  if '670' in update[0][6]:
      write_msg_attach(user_id,
                       'Уделывает 760, но на 1 фазу питания меньше',
                       'photo261166398_456239832')
  if '680' in update[0][6]:
      write_msg_attach(user_id,
                       'Неплохая карта, хоть и жрёт 200вт',
                       'photo261166398_456239834')
  if '750ti' in update[0][6]:
      write_msg_attach(user_id,
                       'Первая карта на архитектуре Maxwell. Затычка, которая +- как GPU PS4',
                       'photo261166398_456239835')
  if '760' in update[0][6]:
      write_msg_attach(user_id,
                       'Неплохая видеокарта для 1600х900, есть версия на 1.5, 2, 3, 4 гига, отличаются шиной. Слабее 670 на 7-10%',
                       'photo261166398_456239836')
  if '770' in update[0][6]:
      write_msg_attach(user_id,
                       'Топ за свои деньги, почти как 1050ти, но жрёт 220вт. Есть версии на 2 и 4 гига',
                       'photo261166398_456239838')
  if '760ti' in update[0][6]:
      write_msg_attach(user_id,
                       'Редкий экземпляр, в России почти нет.',
                       'photo261166398_456239837')
  if '780' in update[0][6]:
      write_msg_attach(user_id,
                       'Прекрасная видеокарта, но жрет 250вт',
                       'photo261166398_456239839')
  if 'r9 270' in update[0][6]:
      write_msg_attach(user_id,
                       'Как 1050, но ценится майнерами. Полный аналог HD 7850, но имеет версию на 4 гига',
                       'photo261166398_456239841')
  if '780ti' in update[0][6]:
      write_msg_attach(user_id,
                       'Тоже ест 250вт, зато как 1060 на 3 гига',
                       'photo261166398_456239840')
  if 'r9_270x' in update[0][6]:
      write_msg_attach(user_id,
                       'Аналог 7870, чуть лучше 1050. Ценится майнерами',
                       'photo261166398_456239842')
  else:
     write_msg(user_id,
     'доступные видеокарты: 650, 650ti, 660, 660ti, 670, 680, 750ti, 760, 760ti, 770, 780, 780ti, r9 270, r9_270x, музыка')
 ts = long_poll['ts']


