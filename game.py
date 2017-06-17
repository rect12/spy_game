from view import View
from data_handler import DataHandler

from vk_helper import newsletter, _vk_autorization
from vk_account import PASSWORD, LOGIN

from random import shuffle


SPY = 'Шпион'


class Game:
    def __init__(self):
        self.epoch_duration = 60
        self.vk_client = _vk_autorization(LOGIN, PASSWORD)
        self.vk_client = _vk_autorization(LOGIN, PASSWORD)
        self.data = DataHandler()
        self.view = View(self, self.data.get_players(),
                         self.data.get_settings())
        self.view.show()


    def set_parametrs(self):
        self.location = self.view.get_location()
        self.roles = self.view.get_roles()
        self.players = self.view.get_players(False)

    def get_players_id(self):
        return [player[1] for player in self.players]

    def to_game(self):
        self.set_parametrs()
        self.roles.append(SPY)
        shuffle(self.roles)
        self.send_roles()


    def send_roles(self):
        role_message = "Твоя роль: {}"
        locaion_message = "\nТекущая локация: {}".format(self.location)
        messages = [role_message.format(role) +
                    ('' if role == SPY else locaion_message)
                    for role in self.roles]
        newsletter(self.vk_client, self.get_players_id(), messages)

    def time_left_newsletter(self, time_left):
        # TODO: add option not to send this every time
        minutes_left = time_left // self.epoch_duration
        if minutes_left > 1 and minutes_left < 5:
            end = 'ы'
        elif minutes_left == 1:
            end = 'а'
        else:
            end = ''

        message = 'Осталось {} минут{}.'.format(minutes_left, end)
        newsletter(self.vk_client, self.get_players_id(), message)

    def game_over(self):
        self.windows['game'].buttons['to main'].show()
        spy_name = self.players[self.roles.index(SPY)][0]
        message = ('Время вышло! Игра окончена. ' +
                   'Победил шпион - {}!'.format(spy_name))
        newsletter(self.vk_client, self.get_players_id(), message)

    def update_data(self):
        self.data.add_location(self.view.get_location(), self.view.get_roles())
        all_players = self.view.get_players(True)
        self.data.rewrite_players(all_players)
