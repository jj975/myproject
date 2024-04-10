import requests
from django.http import HttpResponse
from myapp.credentials import TELEGRAM_API_URL, URL


def setmycommands(request):
    commands = [
        {"command": "start", "description": "Почати використання бота"},
        {"command": "help", "description": "Отримати допомогу з використанням бота"},
        {"command": "register", "description": "Зараєструватись до бота"},
        # Додаткові команди можна додати аналогічно
    ]

    data = {"commands": commands}

    response = requests.post(
        f"{TELEGRAM_API_URL}setMyCommands?url={URL}", json=data).json()

    return HttpResponse(f"{response}")


def clearmycommands(request):
    commands = []
    data = {"commands": commands}

    response = requests.post(
        f"{TELEGRAM_API_URL}setMyCommands?url={URL}", json=data).json()

    return HttpResponse(f"{response}")
