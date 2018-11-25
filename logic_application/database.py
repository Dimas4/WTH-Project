import csv
import datetime
from WTH.wsgi import application
from django.utils import timezone
from wth_base.models import User, Location, Stop
from logic_application.stops_graph import bfs

stops_loaded = False    # цэ костыль оставьте его в покое


def push_database(data: dict):
    try:
        User.objects.create(user_telegram_id=data['chat']['id'])
    except Exception as _er:
        pass


def gen_answer(use, *args, **kwargs):
    global stops_loaded
    if not stops_loaded:
        try:
            load_stops('0list.csv')
            stops_loaded = True
        except:
            pass

    func = _use[use]
    return func(*args, **kwargs)


def add(msg, user_id):
    msg = msg if msg != '/add' else None
    success = 'успешно добавлено'
    error = 'ошибка'
    if not msg or not Stop.objects.filter(name=msg):
        return error

    Location.objects.create(user=User.objects.get(user_telegram_id=user_id), stop_name=msg)
    return success


def view(msg, *args, **kwargs):
    msg = msg if msg != '/view' else None
    success = ['Есть', 'Нет']
    error = 'ошибка'
    if not msg or not Stop.objects.filter(name=msg):
        return error

    dist, name, flag = bfs(msg)
    if not flag:
        return success[1]
    return f"Ближайштй контролер на остановке {name}(в {dist} остановках от вас)"


def report(msg, *args, **kwargs):
    msg = msg if msg != '/report' else None
    success = 'Соощение добавлено'
    error = ['Что-то пошло не так:( Проверьте сообщение, которое вы ввели', 'Такой отметке пока нет']
    if not msg or not Stop.objects.filter(name=msg):
        return error[0]
    locs = Location.objects.filter(stop_name=msg, created_on__gte=timezone.now() - datetime.timedalta(minutes=3))
    for loc in locs:
        loc.user.fake_count += 1
        loc.user.save()
    if not locs:
        return error[1]
    else:
        return success


def load_stops(filename):
    with open(filename, encoding='utf-8') as stops_file:
        stops_csv = csv.reader(stops_file, delimiter='\t')

        for row in stops_csv:
            if row[0] == 'ID':  # skip first row
                continue

            Stop.objects.create(stop_id=int(row[0]), name=row[4], linked_stops=row[8])


_use = {
    'add': add,
    'view': view,
    'report': report,
}
