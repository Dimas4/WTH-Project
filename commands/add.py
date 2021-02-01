from logic_application.database import gen_answer

import command_system


def add(*args, **kwargs):
    message = gen_answer('add', *args, **kwargs)
    return message, [], [], []


add_command = command_system.Command()

add_command.keys = ["/add"]
add_command.description = "Добавить локацию надзирающего. Пр: /add <Прыпынак>"
add_command.process = add
