import random
import requests
import vk_api
from config import *

def write_msg(user_id, text):
  vk_bot.method('messages.send', {'user_id': user_id, 'message': text, 'random_id': random.randint(0, 100000)})
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
 try:
  long_poll = requests.get('https://{server}?act={act}&key={key}&ts={ts}&wait=100100000000'.format(server=server,
                                                                                        act='a_check',
                                                                                        key=key,
                                                                                        ts=ts)).json()

  update = long_poll['updates']
  if update[0][0] == 4:
  #print(update)
   user_id = update[0][3]
   user_name = vk_bot.method('users.get', {'user_ids': user_id})
   print(str(user_name[0]['first_name']) + ' ' + str(user_name[0]['last_name']) + ' написал(а) боту - ' + str(update[0][6]))
   if update[0][6]=='650':
       write_msg_attach(user_id,
                      'Затычка',
                      'photo261166398_456239824')
   elif update[0][6]=='660ti':
       write_msg_attach(user_id,
                      'Лучше 750ти на 2-3 фпс, особенно в 1920х1080',
                      'photo261166398_456239827')
   if update[0][6]=='660':
       write_msg_attach(user_id,
                       'Как 750ти, но шина шире',
                       'photo261166398_456239833')
   elif update[0][6]=='650ti':
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
   if update[0][6]=='760':
       write_msg_attach(user_id,
                       'Неплохая видеокарта для 1600х900, есть версия на 1.5, 2, 3, 4 гига, отличаются шиной. Слабее 670 на 7-10%',
                       'photo261166398_456239836')
   if '770' in update[0][6]:
       write_msg_attach(user_id,
                       'Топ за свои деньги, почти как 1050ти, но жрёт 220вт. Есть версии на 2 и 4 гига',
                       'photo261166398_456239838')
   elif update[0][6]=='760ti':
       write_msg_attach(user_id,
                       'Редкий экземпляр, в России почти нет.',
                       'photo261166398_456239837')
   if update[0][6]=='780':
       write_msg_attach(user_id,
                       'Прекрасная видеокарта, но жрет 250вт',
                       'photo261166398_456239839')
   if 'R9 270' in update[0][6]:
       write_msg_attach(user_id,
                       'Как 1050, но ценится майнерами. Полный аналог HD 7850 и R9 370, но имеет версию на 4 гига',
                       'photo261166398_456239841')
   elif update[0][6]=='780ti':
       write_msg_attach(user_id,
                       'Тоже ест 250вт, зато как 1060 на 3 гига',
                       'photo261166398_456239840')
   if 'R9_270x' in update[0][6]:
       write_msg_attach(user_id,
                       'Аналог 7870 и R9 370x, чуть лучше 1050. Ценится майнерами',
                       'photo261166398_456239842')
   if 'R9 280' in update[0][6]:
       write_msg_attach(user_id,
                       'Аналог HD 7950 и R9 380, но у 380 версии на 2 и 4 гига. Ценится майнерами',
                       'photo261166398_456239843')
   if 'R9_280x' in update[0][6]:
       write_msg_attach(user_id,
                       'Аналог HD 7970 и R9 380x, 380x отличается памятью',
                       'photo261166398_456239844')
   if 'R9 290' in update[0][6]:
       write_msg_attach(user_id,
                       'Первая карта от AMD, которая тянула 4к и тянет. Ест около 300вт, аналог R9 390',
                       'photo261166398_456239845')
   if 'RX 550' in update[0][6]:
       write_msg_attach(user_id,
                       'Самая бесполезная карта. Имеет версии с 512 и 640 шейдерами, плюс 2 или 4 гига',
                       'photo261166398_456239851,photo261166398_456239852')
   if 'RX 560' in update[0][6]:
       write_msg_attach(user_id,
                       'Перевыпуск RX 560 с небольшим разгоном и разблокированными шейдерами(можно было анлокнуть самому)',
                       'photo261166398_456239847')
   if 'RX_560d' in update[0][6]:
       write_msg_attach(user_id,
                       'Полный аналог RX 460, есть версии на 2 и 4 гига',
                       'photo261166398_456239848')
   if 'RX 570' in update[0][6]:
       write_msg_attach(user_id,
                       'Не очень популярный аналог RX 470. Есть версии на 4 и 8 гигов',
                       'photo261166398_456239850')
   if 'RX 580' in update[0][6]:
       write_msg_attach(user_id,
                       'Популярный аналог RX 480. Имеет версии на 4 и 8 гигов',
                       'photo261166398_456239849')
   if update[0][6]=='Vega 56':
       write_msg_attach(user_id,
                       'Видеокарта, имеющая память HBM2 и съедавшая около 250вт, но при этом проигрывает 1080',
                       'photo261166398_456239854')
   if update[0][6] == 'Vega 64':
       write_msg_attach(user_id,
                      'Имеет память HBM2 и жрёт около 300вт, но при этом проигрывает 1080ti',
                      'photo261166398_456239856')
   if '950' in update[0][6]:
       write_msg_attach(user_id,
                       'Наислабейший представитель 2-го прихода Максвелл.Затычка для 1080p, имеет версии на 2 и 4 гига',
                       'photo261166398_456239853')
   if '960' in update[0][6]:
       write_msg_attach(user_id,
                       'Видеокарта уровня 1050ti, иногда чуть слабее, есть версии на 2 и 4 гига. На картинке скрин моего видеоадптера',
                       'photo261166398_456239858')
   if '970' in update[0][6]:
       write_msg_attach(user_id,
                       'Карта с заводским косяком, из-за которого доступно 3.5 гига вместо 4. Производительность как 1063',
                       'photo261166398_456239859')
   if update[0][6]=='980':
       write_msg_attach(user_id,
                        'Карта, которая почти догоняет 1070',
                        'photo261166398_456239866')
   if update[0][6]=='980ti':
       write_msg_attach(user_id,
                       'Карта, которая достойно тянет 4к и сейчас. Является обрубком Titan X, плюс жрёт 250вт',
                       'photo261166398_456239868')
   if '1030' in update[0][6]:
       write_msg_attach(user_id,
                        'Затычка, которая умудряется тащить игры. +- как 560ti, но имеет 64х битную шину',
                        'photo261166398_456239869')
   if update[0][6]=='1050':
       write_msg_attach(user_id,
                        'Затычка',
                        'photo261166398_456239870')
   if update[0][6]=='1050ti':
       write_msg_attach(user_id,
                        'Лучше, чем 960 и Rx 560, но еще затычка',
                        'photo261166398_456239871')
   if update[0][6] == '1063':
       write_msg_attach(user_id,
                       'Топ для 1920x1080',
                       'photo261166398_456239872')
   if update[0][6] == '1066':
       write_msg_attach(user_id,
                       'Топ для 1920x1080, да и в 2560х1440 может. Имееет больше шейдерных блоков и TMU, нежели версия на 3 гига',
                       'photo261166398_456239873')
   if update[0][6]=='1070':
       write_msg_attach(user_id,
                        'Карта с запасом для 1920x1080 и оптимальная для QuadHD',
                        'photo261166398_456239874')
   if update[0][6]=='1070ti':
       write_msg_attach(user_id,
                       'Карта для QuadHD',
                       'photo261166398_456239875')
   if update[0][6]=='1080':
       write_msg_attach(user_id,
                        'Билет в 4к 60fps',
                        'photo261166398_456239876')
   if update[0][6]=='1080ti':
       write_msg_attach(user_id,
                        'Карта с запасом даже для 4к, но и жрет 250вт',
                        'photo261166398_456239877')
   if update[0][6]=='200GE':
       write_msg_attach(user_id,
                        'Как гиперпень, только круче. Гонится на любой плате',
                        'photo261166398_456239883')
   if update[0][6] == 'R3 1200':
       write_msg_attach(user_id,
                        'Бюджетный райзен 1-го поколения. В начале производства имел брак в виде 8 ядер',
                        'photo261166398_456239882')
   if update[0][6]=='R3 1300x':
       write_msg(user_id,
                        'Оерклокнутый 1200, нет смысла в покупке')
   if update[0][6]=='R3 2200G':
       write_msg_attach(user_id,
                        'Второе поколение райзенов. Имеет всроенное видеоядро. В стоке 3.5 ггц',
                        'photo261166398_456239886')
   if update[0][6]=='R5 1400':
       write_msg_attach(user_id,
                        'Имеет SMT, в отличии от 1200',
                        'photo261166398_456239884')
   if update[0][6]=='R5 2400G':
       write_msg_attach(user_id,
                        '8 потоков, встройка на уровне GT 1030, но если оверклокнуть... Что еще нужно в ультрабюджет?',
                        'photo261166398_456239887')
   if update[0][6]=='R5 1500x':
      write_msg(user_id,
                 'Тоже немного оверклокнутый и бессмысленный')
   if update[0][6]=='R5 1600':
       write_msg_attach(user_id,
                        '6 ядер и 12 потоков для народа. Стоковая частота-3.2ггц',
                        'photo261166398_456239885')
   if update[0][6]=='R5 1600x':
       write_msg_attach(user_id,
                        'Чуть подразогнанней и дешевле(на КУ). В стоке 3.6ггц',
                        'photo261166398_456239888')
   if update[0][6]=='R5 2600':
       write_msg_attach(user_id,
                        'Тот же 1600, но уже 2-ое поколение, да и стоит дороже',
                        '')
   if update[0][6]=='1':
      write_msg(user_id,
            'GTX на архитектуре Kepler: 650, 650ti, 660, 660ti, 670, 680, 760, 760ti, 770, 780, 780ti ')
   if update[0][6]=='2':
      write_msg(user_id,
                'Карты на архитектуре GCN: R9 270, R9_270x, R9 280, R9_280x, R9 290, R9_290x, RX 550, RX 560, RX_560d, RX 570, RX 580, Vega 56, Vega 64')
   if update[0][6]=='3':
      write_msg(user_id,
                'Карты на архитектуре Максвелл: 750ti, 950, 960, 970, 980, 980ti')
   if update[0][6]=='4':
        write_msg(user_id,
                  'Карты на архитектуре Паскаль: 1030, 1050, 1050ti, 1063, 1066, 1070, 1070ti, 1080, 1080ti')
   if update[0][6] == '5':
        write_msg(user_id,
                      'Сокет АМ4: 200GE, R3 1200, R3 1300x, R3 2200G, R5 1400, R5 2400G, R5 1500x, R5 1600')
   else:
       write_msg(user_id,
        'Видеокарты: 1, 2, 3, 4; процы: 5 (я не знаю, как сделать так, чтобы он отвечал всем сразу)')
  ts = long_poll['ts']
 except KeyError:
  vk_bot.method('messages.getLongPollServer', {'need_pts': 1, 'lp_version': 3})
  long_poll = requests.get('https://{server}?act={act}&key={key}&ts={ts}&wait=100100000000'.format(server=server,
                                                                                                   act='a_check',
                                                                                                   key=key,
                                                                                                   ts=ts)).json()


