from typing import Text
import telebot
from telebot import types


bot = telebot.TeleBot('1828272395:AAHcVtHnSQb6UFx3jZd0_uMcmptmXrHLeoU')

flag = '✔️'
todo_list = []
last_completed = 'a'

markp = types.ReplyKeyboardMarkup()
yes_btn = types.KeyboardButton('Да')
no_btn = types.KeyboardButton('Нет')
markp.row(yes_btn, no_btn)

markup = types.ReplyKeyboardMarkup()
add_btn = types.KeyboardButton('Добавить')
del_btn = types.KeyboardButton('Удалить')
complete_btn = types.KeyboardButton('Выполнено')
list_btn = types.KeyboardButton('Показать список')
markup.row(add_btn, del_btn)
markup.row(complete_btn, list_btn)

#@bot.callback_query_handler(func=lambda call: True)
###    logger.info(call)

@bot.message_handler(content_types=['text'])
def send_welcome(message):
    chat_id = message.chat.id
    if message.text == "Добавить":
        send = bot.send_message(chat_id, "Какую задачу вы хотите добавить?")
        bot.register_next_step_handler(send, task_add)
    elif message.text == "Удалить":
        send = bot.send_message(chat_id, "Какую задачу вы хотите удалить?")
        bot.register_next_step_handler(send, task_delete)
    elif message.text == "Выполнено":
        send = bot.send_message(chat_id, "Какую задачу вы выполнили?")
        bot.register_next_step_handler(send, task_complete)
        last_completed = send
        show_list(chat_id)
    elif message.text == "Показать список":
        send = bot.send_message(chat_id, 'Список ваших задач:', reply_markup=markup)
        show_list(chat_id)
    elif message.Text == "Да":
        bot.register_next_step_handler(last_completed, task_delete)



def task_add(message):
    task = message.text
    if task in todo_list:
        bot.send_message(message.chat.id, 'Такая задача уже есть!', reply_markup=markup)
    else:
        todo_list.append(task)
        bot.send_message(message.chat.id, 'Задача ' + task + ' добавлена', reply_markup=markup)


def task_delete(message):
    task = message.text
    taskf = message.text + flag
    if len(todo_list) == 0:
        show_list(message.chat.id)
    elif task in todo_list:
        todo_list.remove(task)
        bot.send_message(message.chat.id, 'Задача ' + task + ' удалена', reply_markup=markup)
    elif taskf in todo_list:
        todo_list.remove(taskf)
        bot.send_message(message.chat.id, 'Задача ' + task + ' удалена', reply_markup=markup)
    else:
        bot.send_message(message.chat.id, 'У вас нет таких задач!', reply_markup=markup)


def task_complete(message):
    if len(todo_list) == 0:
        bot.send_message(message.chat.id, 'Как ты мог что-то выполнить, если список пуст?', reply_markup=markup)
    elif message.text in todo_list:
        task = todo_list.index(message.text)
        todo_list[task] = message.text + flag
        bot.send_message(message.chat.id, 'Задача ' + message.text + ' выполнена!')
        # answer = bot.add_poll_answer_handler(message.chat.id, 'Хотите удалить ее?', reply_markup=markp)
        # if answer.text == 'Да':
        #     task_delete(task)
        # elif answer.text == "Нет":
        #     bot.send_message(task.chat.id, ' Ваше право)', reply_markup=markup)
    else:
        bot.send_message(message.chat.id, 'У вас нет такой задачи!', reply_markup=markup)


# def redirect(task):
#     answer = bot.reply_to(task.chat.id, 'Хотите удалить ее?', reply_markup=markp)
#     print(answer)
#     if answer.text == 'Да':
#         task_delete(task)
#     elif answer.text == "Нет":
#         bot.send_message(task.chat.id, ' Ваше право)', reply_markup=markup)


def show_list(chat_id):
    if len(todo_list) == 0:
        bot.send_message(chat_id, 'Ваш список пуст!', reply_markup=markup)
    else:
        str_list = '\n'.join(todo_list)
        bot.send_message(chat_id, str_list, reply_markup=markup)



bot.polling()
