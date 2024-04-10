import requests
from django.http import HttpResponse
from myapp.credentials import TELEGRAM_API_URL, URL


def setwebhook(request):
    response = requests.post(
        TELEGRAM_API_URL + "setWebhook?url=" + URL).json()
    return HttpResponse(f"{response}")


def deletewebhook(request):
    response = requests.post(
        TELEGRAM_API_URL + "deleteWebhook?url=" + URL).json()
    return HttpResponse(f"{response}")
