from WTH.wsgi import application
from wth_base.models import User, Location


def push_database(data: dict):
    try:
        User.objects.create(user_telegram_id=data['chat']['id'])
    except Exception as _er:
        print(_er)
        pass


def gen_answer(use, *args, **kwargs):
    func = _use[use]
    return func(*args, **kwargs)


def add(msg, user_id):
    success = 'успешно добавлено'
    error = 'ошибка'
    Location.objects.create(user_telegram_id=user_id, stop_name=msg)
    return success


def view(msg, *args, **kwargs):
    success = ['Есть', 'Нет']
    error = 'ошибка'
    loc = Location.objects.filter(stop_name=msg, visible=True)
    if loc:
        return success[0]
    else:
        return success[1]


def report(*args, **kwargs):
    success = 'Соощение добавлено'
    error = 'Что-то пошло не так:( Проверьте сообщение, которое вы ввели'
    return error


_use = {
    'add': add,
    'view': view,
    'report': report,
}
