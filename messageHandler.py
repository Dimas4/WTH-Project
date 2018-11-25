import importlib
import time
import os

from logic_application.telegramapi import Telegram
from command_system import command_list


def load_modules():
    files = os.listdir("commands")
    modules = filter(lambda x: x.endswith(".py"), files)
    for m in modules:
        importlib.import_module("commands." + m[0:-3])


def get_answer(user_id, action, content=None):
    message = "Прости, не понимаю тебя. Напиши '/help', чтобы узнать мои команды"
    for c in command_list:
        for k in c.keys:
            if action == k:
                return c.process(content, user_id) if content else c.process(action, user_id)
    return message, "", [], []


def _action_detect(action, data_text):
    text = None
    if action.startswith('/'):
        action = action.split(' ')[0]
        text = data_text[len(action):].strip()
    return action, text


def create_answer(data, token, *args, **kwargs):
    load_modules()
    tg = Telegram(token)
    user_id = data["chat"]["id"]
    action = data.get("text", '')

    # распознование команд
    action, text = _action_detect(action, action)

    args = get_answer(user_id, action, text)
    tg.send_message(user_id, 'Idite na*yi, oplachivaite proezd.', [], [], [])
    time.sleep(1)
    tg.send_message(user_id, 'Eto shutka. Sore za mat', [], [], [])
    time.sleep(1)
    tg.send_message(user_id, args[0], args[1], args[2], args[3])
