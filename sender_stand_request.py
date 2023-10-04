import requests
import config
import data

# Создание заказа

def post_new_order(order_body):
    return requests.post(config.URL_SERVICE + config.CREATE_ORDER_PATH,
                         json=order_body,
                         headers=data.headers)

# Получение данных о заказе по треку заказа

def get_order_from_track(track):
    return requests.get(config.URL_SERVICE +config.FIND_ORDER_FROM_TRACK_PATH + str(track),
                        headers=data.headers)