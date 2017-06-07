import vk_api
import time


SPY = 'Шпион'


def _vk_autorization(login, password):
    """
    Returns client authtorized with login and password
    """
    vk = vk_api.VkApi(login=login, password=password)
    vk.auth()
    return vk


def _write_vk_message(vk, user_id, message):
    """
    Sends message to user with user_id from client
    """
    vk.method('messages.send',
              {'user_id': user_id,
               'message': message})


def send_roles(login, password, users_id, location, roles):
    """
    Send roles to players with users_id
    """
    vk = _vk_autorization(login, password)
    for user, role in zip(users_id, roles):
        message = "Твоя роль: {}".format(role, location)
        if role == SPY:
            _write_vk_message(vk, user, message)
        else:
            message += "\nТекущая локация: {}".format(role, location)
            _write_vk_message(vk, user, message)
        time.sleep(0.5)
