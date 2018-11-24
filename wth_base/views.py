from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

import json

from logic_application.database import push_database
from settings import *
import messageHandler


def hello_world(request):
    return HttpResponse("Hello from Django!")


@csrf_exempt
def telegram(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        if data.get("message"):
            push_database(data["message"])
            messageHandler.create_answer(
                data["message"], config['app']['tg']['token']
            )
            return HttpResponse("ok")
        return HttpResponse("nothing")
