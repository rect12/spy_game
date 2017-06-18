import vk_api
import time


def vk_autorization(login, password):
    """
    Returns client authtorized with login and password
    """
    vk = vk_api.VkApi(login=login, password=password)
    vk.auth()
    return vk


def write_vk_message(vk, user_id, message):
    """
    Sends message to user with user_id from client
    """
    vk.method('messages.send',
              {'user_id': user_id,
               'message': message})


def newsletter(vk_client, users_id, messages):
    """
    Sends messages to users with users_id.

    If messages is str sends this message to all players
    """
    if isinstance(messages, str):
        messages = [messages] * len(users_id)

    for user_id, message in zip(users_id, messages):
        write_vk_message(vk_client, user_id, message)
        time.sleep(0.5)
