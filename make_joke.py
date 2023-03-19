import anecdotica as acalib
import os
from dotenv import load_dotenv

load_dotenv()

# настройки профиля
USER_PROFILE = {
    'http_method': 'GET',  # выбранный http-метод (POST | GET)
    'pid': os.getenv('PID'),  # идентификатор профиля (логин)
    'key': os.getenv('KEY')
    # секретный ключ
}
API_SETTINGS = {  # настройки запроса
    'genre': 1,
    'lang': 1,
    'note': 1,
    'markup': 0
}


def get_joke():
    reply = acalib.RandomItemApi.get_reply(USER_PROFILE, API_SETTINGS)
    if reply.is_error():  # если ошибка
        # обрабатываем ошибку
        print(reply.get_result().get_error(), reply.get_result().get_err_msg())
    else:  # если нет ошибки
        # выводим полученную запись
        # print(reply.get_item().get_text(), reply.get_item().get_note())
        return reply.get_item().get_text()


if __name__ == '__main__':
    get_joke()
