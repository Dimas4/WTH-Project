from logic_application.database import gen_answer

import command_system


def report(*args, **kwargs):
    message = gen_answer('report', *args, **kwargs)
    return message, [], [], []


report_command = command_system.Command()

report_command.keys = ["/report"]
report_command.description = ""
report_command.process = report
