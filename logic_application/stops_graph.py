import datetime
from WTH.wsgi import application
from django.utils import timezone

from wth_base.models import Stop, Location


def bfs(stop):  # обход в ширину
    dist = 0

    used = set()
    next_stops = []

    next_stops.extend(map(lambda x: x.stop_id, Stop.objects.filter(name=stop)))

    for i in next_stops:
        used.add(i)

    while True:
        temp = []

        for stop_id in next_stops:
            stop = Stop.objects.get(stop_id=stop_id)

            if Location.objects.filter(visible=True, stop_name=stop.name, created_on__gte=timezone.now() - datetime.timedelta(minutes=3)):
                return dist, stop.name, True

            linked = filter(lambda x: x not in used, map(int, stop.linked_stops.split(',')))
            temp.extend(linked)

            for i in temp:
                used.add(i)
        if not temp:
            return -1, '', False

        next_stops = temp
        dist += 1
