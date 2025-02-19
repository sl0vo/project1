import telebot
import sqlite3
from telebot import types
from datetime import datetime, timedelta

bot = telebot.TeleBot('7664389350:AAEr3GoUP7V3oju5DbTKEP9nUZzMbUlCCq0')
YOUR_CHAT_ID = '1734603916'

connection = sqlite3.connect('my_database.db', check_same_thread=False)
cursor = connection.cursor()
selected_date = None
selected_time = None
info = None
car_info = {}

# cursor.execute('''
# CREATE TABLE IF NOT EXISTS Users (
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     user_id INTEGER UNIQUE,
#     username TEXT NOT NULL,
#     number_phone TEXT NOT NULL,
#     date_record TEXT NOT NULL,
#     time_record TEXT NOT NULL
# )
# ''')

connection.commit()


def start():
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton(text='Записаться на технический осмотр', callback_data='clc 1')
    btn2 = types.InlineKeyboardButton(text='Подробнее о нас', callback_data='clc 2')
    markup.add(btn1, btn2)
    return markup

def start1():
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton(text='Хорошо', callback_data='clcс 1')
    btn2 = types.InlineKeyboardButton(text='Назад', callback_data='clc 23')
    markup.add(btn1, btn2)
    return markup

def questions1():
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton(text='Легковые авто', callback_data='clc 11')
    btn2 = types.InlineKeyboardButton(text='Грузовые авто', callback_data='clc 12')
    markup.add(btn1, btn2)
    return markup

def get_car_info(message):
    global car_info
    global info
    chat_id = message.chat.id
    car_info[chat_id] = message.text  # Сохраняем информацию об авто
    info = car_info[chat_id]
    bot.send_message(chat_id, f"Присутствует ли трещина на лобовом стекле и фарах?", reply_markup=reply1())


def questions2():
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton(text='Адрес', callback_data='clc 21')
    btn2 = types.InlineKeyboardButton(text='Сайт', url='https://techosmotr.wixsite.com/fili')
    btn3 = types.InlineKeyboardButton(text='Главное меню', callback_data='clc 23')
    markup.add(btn1, btn2, btn3)
    return markup


def reply1():
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton(text='Отсутствует', callback_data='otvet_ok')
    btn2 = types.InlineKeyboardButton(text='Присутствует', callback_data='otvet_notok')
    markup.add(btn1, btn2)
    return markup


def reply2():
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton(text='Отсутствует', callback_data='otvet_ok1')
    btn2 = types.InlineKeyboardButton(text='Присутствует', callback_data='otvet_notok')
    markup.add(btn1, btn2)
    return markup

def reply3():
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton(text='Отсутствует', callback_data='otvet_ok2')
    btn2 = types.InlineKeyboardButton(text='Присутствует', callback_data='otvet_notok')
    markup.add(btn1, btn2)
    return markup


# def end_information():
#     markup = types.InlineKeyboardMarkup()
#     btn1 = types.InlineKeyboardButton(text='Адрес', callback_data='clc 212')
#     btn2 = types.InlineKeyboardButton(text='Сайт', url='https://yandex.ru/maps/-/CDxpq6nI')
#     btn3 = types.InlineKeyboardButton(text='Назад', callback_data='clc 222')
#     markup.add(btn1, btn2, btn3)
#     return markup


def date():
    markup = types.InlineKeyboardMarkup()
    today = datetime.today()
    tomorrow = today + timedelta(days=1)
    btn1 = types.InlineKeyboardButton(text=f"Сегодня {today.strftime('%Y-%m-%d')}", callback_data="today")
    btn2 = types.InlineKeyboardButton(text=f"Завтра {tomorrow.strftime('%Y-%m-%d')}", callback_data="tomorrow")
    markup.add(btn1, btn2)
    return markup


def time_today():
    markup = types.InlineKeyboardMarkup()
    now = datetime.now().time()
    time_slots = ['00:00', '00:30', '01:00', '01:30', '02:00', '02:30', '03:00', '03:30', '04:00', '04:30',
                  '05:00', '05:30', '06:00', '06:30', '07:00', '07:30', '08:00', '08:30', '09:00', '09:30',
                  '10:00', '10:30', '11:00', '11:30', '12:00', '12:30', '13:00', '13:30', '14:00', '14:30',
                  '15:00', '15:30', '16:00', '16:30', '17:00', '17:30', '18:00', '18:30', '19:00', '19:30',
                  '20:00', '20:30', '21:00', '21:30', '22:00', '22:30', '23:00', '23:30']

    busy_slots = cursor.execute('SELECT time_record FROM Users WHERE date_record = ?',
                                (datetime.now().date().strftime('%Y-%m-%d'),)).fetchall()
    busy_slots = [slot[0] for slot in busy_slots]

    for elem in time_slots:
        if elem > now.strftime('%H:%M') and elem not in busy_slots:
            btn = types.InlineKeyboardButton(text=elem, callback_data=f'timeZapisi_{elem}')
            markup.add(btn)

    return markup


def time_tomorrow():
    markup = types.InlineKeyboardMarkup()
    tomorrow = (datetime.now() + timedelta(days=1)).date()
    time_slots = ['00:00', '00:30', '01:00', '01:30', '02:00', '02:30', '03:00', '03:30', '04:00', '04:30',
                  '05:00', '05:30', '06:00', '06:30', '07:00', '07:30', '08:00', '08:30', '09:00', '09:30',
                  '10:00', '10:30', '11:00', '11:30', '12:00', '12:30', '13:00', '13:30', '14:00', '14:30',
                  '15:00', '15:30', '16:00', '16:30', '17:00', '17:30', '18:00', '18:30', '19:00', '19:30',
                  '20:00', '20:30', '21:00', '21:30', '22:00', '22:30', '23:00', '23:30']

    busy_slots = cursor.execute('SELECT time_record FROM Users WHERE date_record = ?',
                                (tomorrow.strftime('%Y-%m-%d'),)).fetchall()
    busy_slots = [slot[0] for slot in busy_slots]

    for elem in time_slots:
        if elem not in busy_slots:
            btn = types.InlineKeyboardButton(text=elem, callback_data=f'timeZapisi_{elem}')
            markup.add(btn)

    return markup


def cancel_recording(time):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton(text='Отменить запись', callback_data=f'cancel_{time}')
    # btn2 = types.InlineKeyboardButton(text='Подробнее о нас', callback_data='clc 221')
    markup.add(btn1)
    return markup


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Добро пожаловать! Выберите опцию:', reply_markup=start())


@bot.message_handler(commands=['admin'])
def start_second_message(message):
    bot.send_message(message.chat.id, 'Добро пожаловать! Введите пароль:')


@bot.message_handler(content_types=['text', 'photo', 'sticker'])
def handle_message(message):
    if message.text == '1111':
        bot.send_message(message.chat.id, 'Отлично. Выберите дату для записи:', reply_markup=date())

@bot.callback_query_handler(func=lambda call: True)
def context(call):
    global selected_time
    global selected_date
    global info
    chat_id = call.message.chat.id

    if call.data == 'clc 1':
        bot.send_message(chat_id, 'Чтобы не терять время и не приезжать к нам напрасно, пожалуйста, ответьте на четыре вопроса.', reply_markup=start1())
        bot.delete_message(chat_id, call.message.message_id)
    if call.data == 'clcс 1':
        bot.send_message(chat_id, 'Какой категории авто?', reply_markup=questions1())
        bot.delete_message(chat_id, call.message.message_id)
    elif call.data == 'clc 2':
        bot.send_message(chat_id, 'Подробные данные о нас:', reply_markup=questions2())
        bot.delete_message(chat_id, call.message.message_id)
    elif call.data == 'clc 21':
        bot.send_message(chat_id, 'Наш адрес: ', reply_markup=questions2())
        bot.delete_message(chat_id, call.message.message_id)
    elif call.data == 'clc 23':
        bot.send_message(chat_id, 'Вы вернулись в главное меню.', reply_markup=start())
        bot.delete_message(chat_id, call.message.message_id)
    elif call.data == 'clc 12':
        bot.send_message(chat_id, 'Вы выбрали грузовые авто. Но на них мы не проводим технический осмотр.')
        bot.send_message(chat_id, 'Вы вернулись в главное меню.', reply_markup=start())
    elif call.data == 'clc 11':
        bot.send_message(chat_id, 'Хорошо. Вы выбрали легковые авто. Напишите марку, модель и год выпуска Т.С.')
        bot.delete_message(chat_id, call.message.message_id)
        bot.register_next_step_handler(call.message, get_car_info)
    elif call.data == 'otvet_notok':
        bot.send_message(chat_id, 'Рекомендуем вам связаться с нашим специалистом по телефону +7 777 77 77.')
        bot.send_message(chat_id, 'Вы вернулись в главное меню.', reply_markup=start())
        bot.delete_message(chat_id, call.message.message_id)
    elif call.data == 'otvet_ok':
        bot.send_message(chat_id, 'Есть ли тонировка на лобовом стекле или стеклах передних сидений?', reply_markup=reply2())
        bot.delete_message(chat_id, call.message.message_id)
    elif call.data == 'otvet_ok1':
        bot.send_message(chat_id, 'Отлично. Имеются ли конструктивные изменнения в Вашем Т.С., а именно силовые бампера, шноркель, экспедиционный багажник, фаркоп и тд.', reply_markup=reply3())
        bot.delete_message(chat_id, call.message.message_id)
    elif call.data == 'otvet_ok2':
        bot.send_message(chat_id, 'Прекрасно! Выберите дату для записи:', reply_markup=date())
        bot.delete_message(chat_id, call.message.message_id)
    # elif call.data == 'clc 221':
    #     bot.send_message(chat_id, 'Подробные данные о нас:', reply_markup=end_information())
    #     bot.delete_message(chat_id, call.message.message_id)
    # elif call.data == 'clc 222':
    #     bot.send_message(chat_id, 'Подробные данные о нас:', reply_markup=cancel_recording(selected_time))
    #     bot.delete_message(chat_id, call.message.message_id)
    # elif call.data == 'clc 212':
    #     bot.send_message(chat_id, 'Наш адрес: ', reply_markup=end_information())
    #     bot.delete_message(chat_id, call.message.message_id)
    elif call.data == 'today':
        bot.send_message(chat_id, 'Выберите время для записи:', reply_markup=time_today())
        bot.delete_message(chat_id, call.message.message_id)
        selected_date = datetime.now().date()

    elif call.data == 'tomorrow':
        bot.send_message(chat_id, 'Выберите время для записи:', reply_markup=time_tomorrow())
        bot.delete_message(chat_id, call.message.message_id)
        date1 = datetime.now().date()
        selected_date = date1 + timedelta(days=1)
    elif call.data.startswith('timeZapisi'):
        selected_time = call.data.split('_')[1]

        cursor.execute('SELECT * FROM Users WHERE user_id = ? AND time_record = ?',
                       (chat_id, selected_time))
        existing_booking = cursor.fetchone()

        if existing_booking:
            bot.send_message(chat_id,
                             'Вы уже записаны на это время. Вы можете отменить запись и выбрать другое время.',
                             reply_markup=cancel_recording(selected_time))
            bot.delete_message(chat_id, call.message.message_id)
        else:
            keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
            phone_button = types.KeyboardButton("Отправить номер телефона", request_contact=True)
            keyboard.add(phone_button)
            bot.send_message(chat_id, f'Вы выбрали время {selected_time}. Пожалуйста, отправьте свой номер телефона c помощью кнопки.',
                             reply_markup=keyboard)


            # Регистрируем следующий шаг, чтобы обработать контакт
            bot.register_next_step_handler(call.message, process_contact, selected_time=selected_time,
                                           selected_date=selected_date)

    elif call.data.startswith('cancel_'):
        time = call.data.split('_')[1]
        cursor.execute('DELETE FROM Users WHERE user_id = ? AND time_record = ?', (chat_id, time))
        connection.commit()
        bot.send_message(chat_id, f'Ваша запись на {time} отменена.')
        bot.send_message(YOUR_CHAT_ID, f'Запись на {time} отменена.')
        bot.delete_message(chat_id, call.message.message_id)
        bot.send_message(chat_id, 'Вы вернулись в главное меню.', reply_markup=start())


def process_contact(message, selected_time, selected_date):
    if message.contact:
        formatted_number = message.contact.phone_number
    else:
        bot.send_message(message.chat.id, 'Пожалуйста, отправьте номер телефона, используя кнопку.')
        return

    user_id = message.from_user.id
    username = message.from_user.username if message.from_user.username else 'Неизвестный'

    cursor.execute('SELECT * FROM Users WHERE user_id = ? AND date_record = ? AND time_record = ?',
                   (user_id, selected_date.strftime('%Y-%m-%d'), selected_time))
    existing_booking = cursor.fetchone()

    if existing_booking:
        bot.send_message(message.chat.id,
                         'Вы уже записаны на это время. Вы можете отменить запись и выбрать другое время.',
                         reply_markup=cancel_recording(selected_time))
        return

    try:
        cursor.execute(
            'INSERT INTO Users (user_id, username, number_phone, date_record, time_record) VALUES (?, ?, ?, ?, ?)',
            (user_id, info, formatted_number, selected_date.strftime('%Y-%m-%d'), selected_time))
        connection.commit()
        bot.send_message(message.chat.id,
                         f'Спасибо! Ваша запись {selected_date} на {selected_time} подтверждена. Наш адрес: Промышленный проезд, дом 3б. Телефон для связи: 79999999999.',
                         reply_markup=cancel_recording(selected_time))
        bot.send_message(YOUR_CHAT_ID,
                         f'Новая запись! Номер телефона: {formatted_number}, Дата: {selected_date}, Время: {selected_time}')

    except sqlite3.IntegrityError as e:
        cursor.execute('SELECT * FROM Users WHERE user_id = ?', (user_id,))
        existing_records = cursor.fetchall()
        print(f"Существующие записи для user_id {user_id}: {existing_records}")  # Лог для отладки
        bot.send_message(message.chat.id,
                         f'Вы уже записаны на другое время : {list(existing_records[-1])[-1]} и дату {list(existing_records[-1])[-2]}. Вы можете отменить запись и выбрать другое время.')
                         #'Произошла ошибка при записи. Пожалуйста, повторите попытку позже.\n' + str(e))


bot.polling(none_stop=True)