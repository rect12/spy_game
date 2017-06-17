import pandas as pd
import numpy as np
import os


class DataHandler:
    def __init__(self):
        self.players_path = 'players.csv'
        self.locations_path = 'locations.csv'
        self.role_delimiter = '###'
        self.separator = '\t'
        self.location_columns = ['Location', 'Roles']
        self.user_columns = ['Name', 'ID']

        self.create_if_not_exist(self.players_path, self.user_columns)
        self.create_if_not_exist(self.locations_path, self.location_columns)

    def create_if_not_exist(self, path, columns):
        if not os.path.exists(path):
            pd.DataFrame(columns=columns).to_csv(path,
                                                 index=False,
                                                 sep=self.separator)

    def add_location(self, location, roles):
        """
        Add location with roles.

        If location already was in dataset update roles to new.
        """
        self._add_to_csv(self.locations_path,
                         [location, self.role_delimiter.join(roles)],
                         self.location_columns[0])

    def _add_to_csv(self, path, row, key_columns):
        old_dataframe = pd.read_csv(path, sep=self.separator)
        columns = old_dataframe.columns
        keys = old_dataframe[key_columns].values.reshape(-1)
        row_key = np.array((row[columns.index(key_column)]
                            for key_column in key_columns))

        if row_key not in keys:
            pd.DataFrame([row]).to_csv(path, sep=self.separator, mode='a',
                                       index=False, header=False)
        else:
            matches = np.where(keys == row_key)[0]
            old_dataframe.drop(matches, inplace=True)
            new_row = pd.DataFrame([row], columns=columns)
            old_dataframe = old_dataframe.append(new_row,
                                                 ignore_index=True)
            old_dataframe.to_csv(path, sep=self.separator, index=False,
                                 mode='w')

    def rewrite_players(self, data):
        self._rewrite_csv(self.players_path, data, self.user_columns)

    def _rewrite_csv(self, path, data, columns):
        new_dataframe = pd.DataFrame(data, columns=columns)
        new_dataframe.to_csv(path, sep=self.separator, index=False, header=True)

    def get_players(self):
        return pd.read_csv(self.players_path, header=0, sep=self.separator).values
