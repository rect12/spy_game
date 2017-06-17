from graphical_interface import WINDOWS, MainWindow, PlayerOptionsWindow
from graphical_interface import GameOptionsWindow, SettingOptionsWindow
from graphical_interface import GameWindow
from vk_helper import newsletter, _vk_autorization
from vk_account import PASSWORD, LOGIN

from random import shuffle
from data_handler import DataHandler


SPY = 'Шпион'


class Game:
    def __init__(self, application):
        self.application = application
        self.vk_client = _vk_autorization(LOGIN, PASSWORD)
        self.epoch_duration = 60
        self.data = DataHandler()

        windows = [MainWindow, PlayerOptionsWindow, GameOptionsWindow,
                   SettingOptionsWindow, GameWindow]
        init_arguments = [{}, {'players': self.data.get_players()}] + [{}]*3

        self.windows = {name: window(self, **kwargs)
                        for name, window, kwargs
                        in zip(WINDOWS, windows, init_arguments)}

        for window in self.windows.values():
            window._post_init()

    def set_parametrs(self):
        self.location = self.get_location()
        self.roles = self.get_roles()
        self.players = self.get_players(False)

    def get_location(self):
        return self.windows['setting options'].line_edits[0].text()

    def get_roles(self):
        return [line_edit.text()
                for line_edit
                in self.windows['setting options'].line_edits[1:-1]]

    def get_duration(self):
        return int(self.windows['game options'].line_edits[0].text())

    def get_players_id(self):
        return [player[1] for player in self.players]

    def get_players(self, need_all):
        players = []
        po_window = self.windows['player options']
        for player_ind in range(len(po_window.line_edits) // 2 - 1):
            name = po_window.line_edits[2*player_ind].text()
            user_id = po_window.line_edits[2*player_ind + 1].text()

            if need_all or po_window.check_boxes[player_ind].isChecked():
                players.append([name, user_id])
        return players

    def to_game(self):
        self.set_parametrs()
        self.roles.append(SPY)
        shuffle(self.roles)

        self.send_roles()

        self.windows['game'].to_game()

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
        self.data.add_location(self.get_location(), self.get_roles())
        all_players = self.get_players(True)
        self.data.rewrite_players(all_players)
