from view import View
from data_handler import DataHandler

from vk_helper import newsletter, vk_autorization, write_vk_message
from vk_account import PASSWORD, LOGIN

from random import shuffle, randint


SPY = 'Шпион'
# TODO: make classes Location and Player


class Game:
    # TODO: add state 'game running'
    def __init__(self):
        self.epoch_duration = 60
        self.vk_client = vk_autorization(LOGIN, PASSWORD)
        self.data = DataHandler()
        self.view = View(self, self.data.get_players(),
                         self.data.get_settings())
        self.view.show()

    def set_parametrs(self):
        self.location = self.view.get_location()
        self.roles = self.view.get_roles()
        self.players = self.view.get_players(False)
        self.first_player = self.choose_first()

    def get_players_id(self):
        return [player[1] for player in self.players]

    def get_players_names(self):
        return [player[0] for player in self.players]

    def to_game(self):
        self.set_parametrs()
        self.roles.append(SPY)
        shuffle(self.roles)
        self.send_start_messages()
        self.update_data()

    def choose_first(self):
        return self.players[randint(0, len(self.players) - 1)]

    def send_start_messages(self):
        role_message = "\nТвоя роль: {}"
        locaion_message = "\nТекущая локация: {}".format(self.location)
        messages = ['Скоро начнется сеанс игры The Spy!' +
                    role_message.format(role) +
                    ('' if role == SPY else locaion_message)
                    for role in self.roles]
        newsletter(self.vk_client, self.get_players_id(), messages)

    def time_left_newsletter(self, time_left):
        # TODO: add option not to send this every time
        minutes_left = time_left // self.epoch_duration

        left_end = 'о'
        if minutes_left > 1 and minutes_left < 5:
            minute_end = 'ы'
        elif minutes_left == 1:
            left_end = 'а'
            minute_end = 'а'
        else:
            minute_end = ''

        message = 'Остал{}сь {} минут{}.'.format(left_end,
                                                 minutes_left,
                                                 minute_end)
        newsletter(self.vk_client, self.get_players_id(), message)

    def game_over(self):
        self.view.game_over()
        spy_name = self.players[self.roles.index(SPY)][0]

        message = ('Время вышло! Игра окончена. ' +
                   'Победил шпион - {}!'.format(spy_name) +
                   '\nВсе это время мы находились в локации ' +
                   '{}'.format(self.location))
        for player, role in zip(self.get_players_names(), self.roles):
            message += '\n{} играл роль "{}"'.format(player, role)

        newsletter(self.vk_client, self.get_players_id(), message)

    def update_data(self):
        self.data.add_location(self.view.get_location(), self.view.get_roles())
        all_players = self.view.get_players(True)
        self.data.rewrite_players(all_players)

    def start_game(self):
        newsletter(self.vk_client, self.get_players_id(), 'Игра началась!')

        message = 'Ты задаешь первый вопрос'
        write_vk_message(self.vk_client, self.first_player[1], message)

        self.view.start_game()
