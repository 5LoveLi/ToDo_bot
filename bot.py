import telebot
from telebot import types

bot = telebot.TeleBot('1616063590:AAHY8PK4cXbFzUngclrwq8b5m7uktvdabeg')

friends_list = {'Надя': 0, 'Соня': 0, 'Вера': 0}

@bot.message_handler(content_types=["text"])
def any_msg(message):
    keyboard = types.InlineKeyboardMarkup()
    callback_button = types.InlineKeyboardButton(text="Да", callback_data="test")
    callback_button1 = types.InlineKeyboardButton(text="Нет", callback_data="test1")
    keyboard.add(callback_button)
    keyboard.add(callback_button1)
    if message.text == "добавить друга":
        send = bot.send_message(message.chat.id, 'как зовут вашего нового друга?')
        bot.register_next_step_handler(send, friend_add)
    elif message.text == "список друзей":
        bot.send_message(message.chat.id, "список ваших друзей:")
        #bot.send_message(message.chat.id, list(friends.keys()))
        bot.send_message(message.chat.id, friends)
    elif message.text == "оценить":
        send = bot.send_message(message.chat.id, 'Кому вы хотите поставить оценку?')
        bot.register_next_step_handler(send, estimation)

    bot.send_message(message.chat.id, "Любишь торт?", reply_markup=keyboard)


def friend_add(message):
    friends = message.text
    if friends in friends_list:
        bot.send_message(message.chat.id, 'Вы ', reply_markup=markup)
    else:
        friends_list.append(friends)
        bot.send_message(message.chat.id, 'Задача ' + friends + ' добавлена', reply_markup=markup)


# В большинстве случаев целесообразно разбить этот хэндлер на несколько маленьких
@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    # Если сообщение из чата с ботом
    if call.message:
        if call.data == "test":
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="я тоже")
        elif call.data == "test1":
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="как так можно!")
    # Если сообщение из инлайн-режима

if __name__ == '__main__':
    bot.infinity_polling()





# friends = {'Надя': 0, 'Соня': 0, 'Вера': 0}

# markup = types.ForceReply(selective=False)

# mark = types.ReplyKeyboardMarkup()
# itembtn1 = types.KeyboardButton('1')
# itembtn2 = types.KeyboardButton('2')
# itembtn3 = types.KeyboardButton('3')
# itembtn4 = types.KeyboardButton('4')
# itembtn5 = types.KeyboardButton('5')
# mark.row(itembtn1, itembtn2, itembtn3)
# mark.row(itembtn4, itembtn5)

# markup = types.ReplyKeyboardMarkup()
# itembtna = types.KeyboardButton('добавить друга')
# itembtnv = types.KeyboardButton('список друзей')
# itembtnc = types.KeyboardButton('оценить')
# markup.row(itembtna, itembtnv)
# markup.row(itembtnc)
# #types.InlineKeyboardButton()




# @bot.message_handler(content_types=['text'])
# def handle_docs_audio(message):
#     if message.text == "Hello":
#       #  print(message.chat.id)
#         bot.reply_to(message, "Hello")
#         bot.send_message()
#     elif message.text == "bay":
#         bot.reply_to(message, "bay")
#     elif message.text == "добавить друга":
#         send = bot.send_message(message.chat.id, 'как зовут вашего нового друга?')
#         bot.register_next_step_handler(send, friend_add)
#     elif message.text == "список друзей":
#         bot.send_message(message.chat.id, "список ваших друзей:")
#         #bot.send_message(message.chat.id, list(friends.keys()))
#         bot.send_message(message.chat.id, friends)
#     elif message.text == "оценить":
#         send = bot.send_message(message.chat.id, 'Кому вы хотите поставить оценку?')
#         bot.register_next_step_handler(send, estimation)


# def estimation(message):
#     friend = message.text.split()[0]
#     bot.send_message(message.chat.id, "какая будет оценка", reply_markup=mark)
#     friends[friend] = message.text.split()[0]


# def friend_add(message):
#     frend = message.text.split()[0]
#     friends[frend] = 0 #len(friends) + 1
#     bot.send_message(message.chat.id, 'друг ' + frend + ' добавлен')

# print(friends)
# print('Started bot pulling ...')
bot.polling()
