#!/usr/bin/python

import PyQt5
from vk_helper import _vk_autorization
from vk_account import LOGIN, PASSWORD
import pandas as pd
from csv_helper import USERS, LOCATIONS, add_user, add_location, SEP
import os


def main():
    if not os.path.exists(LOCATIONS):
        pd.DataFrame(columns=['Location', 'Role']).to_csv(LOCATIONS,
                                                          index=False,
                                                          sep=SEP)
    if not os.path.exists(USERS):
        pd.DataFrame(columns=['Name', 'ID']).to_csv(USERS,
                                                    index=False,
                                                    sep=SEP)

    vk = _vk_autorization(LOGIN, PASSWORD)
    add_location('Joke', ['3', '2'])
    users = pd.read_csv(LOCATIONS, sep=SEP)
    print(users.values)

if __name__ == '__main__':
    main()
