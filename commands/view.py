from logic_application.database import gen_answer

import command_system


def view(*args, **kwargs):
    message = gen_answer('view', *args, **kwargs)
    return message, [], [], []


view_command = command_system.Command()

view_command.keys = ["/view"]
view_command.description = ""
view_command.process = view
