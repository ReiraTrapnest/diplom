# Руслана Рысс, поток 08-a, venus — Финальный проект. Инженер по тестированию плюс

import data
import sender_stand_request

# Получение данных заказа из трека

def assertion_code_200():
    response_pno = sender_stand_request.post_new_order(data.order_body)
    track = response_pno.json()["track"]
    return sender_stand_request.get_order_from_track(track).status_code

# Автоматическое получение данных заказа из трека

def test_order_from_track_code_200():
    assert assertion_code_200() == data.status_code_successful