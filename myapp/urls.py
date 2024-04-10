from django.urls import path
from . import views, testviews, webhook, mycommands

urlpatterns = [
    path('getpost/', views.telegram_bot, name='telegram_bot'),
    # path('getpost/', testviews.telegram_bot, name='telegram_bot'),
    path('setwebhook/', webhook.setwebhook, name='setWebhook'),
    path('deletewebhook/', webhook.deletewebhook, name='deleteWebhook'),
    path('setmycommands/', mycommands.setmycommands, name='setMyCommands'),
    path('setmycommands/', mycommands.clearmycommands, name='claerMyCommands'),
]
