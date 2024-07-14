#Табинаев Санжай, 18+-я когорта, Инженер по тестированию плюс. Дипломный проект
import request

def test_order_creation():
    creation_response = request.post_new_order()
    track_id = creation_response.json()['track']
    response = request.get_orders_track(track_id)
    assert response.status_code == 200