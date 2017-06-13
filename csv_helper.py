import pandas as pd
import numpy as np


USERS = 'users.csv'
LOCATIONS = 'locations.csv'
ROLE_DELIMITER = '###'
SEP = '\t'


def add_user(name, ID):
    """
    Add user with ID.

    If user already was in dataset update ID to new.
    """
    _add_to_csv(USERS, [name, ID])


def add_location(location, roles=[]):
    """
    Add location with roles.

    If location already was in dataset update roles to new.
    """
    _add_to_csv(LOCATIONS, [location, ROLE_DELIMITER.join(roles)])


def _add_to_csv(path, row):
    old_dataframe = pd.read_csv(path, sep=SEP)
    columns = old_dataframe.columns
    keys = old_dataframe[columns[0]].values.reshape(-1)

    if row[0] not in keys:
        pd.DataFrame([row]).to_csv(path, sep=SEP, mode='a',
                                   index=False, header=False)
    else:
        matches = np.where(keys == row[0])[0]
        old_dataframe.drop(matches, inplace=True)
        new_row = pd.DataFrame([row], columns=columns)
        old_dataframe = old_dataframe.append(new_row,
                                             ignore_index=True)
        old_dataframe.to_csv(path, sep=SEP, index=False, mode='w')

def _to_csv(path, data):
    old_dataframe = pd.read_csv(path, sep=SEP, header=0)
    columns = old_dataframe.columns
    new_dataframe = pd.DataFrame(data, columns=columns)
    new_dataframe.to_csv(path, sep=SEP, index=False, header=True)
