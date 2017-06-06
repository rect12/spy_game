import vk_api
import time


def _vk_autorization(login, password):
    vk = vk_api.VkApi(login=login, password=password)
    vk.auth()
    return vk


def _write_vk_message(vk, user_id, role, location=''):
    vk.method('messages.send',
              {'user_id': user_id,
               'message': "Твоя роль: {} \n \
                           Текущая локация: {}".format(role, location)})


def send_roles(login, password, users_id, location, roles):
    vk = _vk_autorization(login, password)
    for user, role in zip(users_id, roles):
        if role == 'Шпион':
            _write_vk_message(vk, user, role, 'кто знает')
        else:
            _write_vk_message(vk, user, role, location)
        time.sleep(0.5)
