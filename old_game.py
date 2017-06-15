#!/usr/bin/python3

import random
import os
import time


def main():
    locations = ['База террористов',
                 'Банк',
                 'Больница',
                 'Киностудия',
                 'Корпоративная вечеринка',
                 'Овощебаза',
                 'Пратизанский отряд',
                 'Пассажирский поезд',
                 'Пиратский корабль',
                 'Полярная станция',
                 'Посольство',
                 'Ресторан',
                 'Супермаркет'
                 'Театр',
                 'Университет',
                 'Воинская часть',
                 'Войско крестоносцев',
                 'Казино',
                 'Океанский лайнер',
                 'Орбитальная станция',
                 'Отель',
                 'Пляж',
                 'Подводная лодка',
                 'Полицейский участок',
                 'Самолет',
                 'Спа-салон',
                 'Станция техобслуживания',
                 'Церковь',
                 'Цирк-шапито',
                 'Школа']

    spy = 'Шпион'
    # location = random.choice(locations)
    # ind = locations.index(location)

    # location = 'Самолет'
    # roles = ['Стюардесса', 'Стюардесса', 'Помощник пилота', 'Пилот',
    #          'Дед, боящийся летать', 'Мама плачущего ребенка',
    #          'Террорист', 'Плачущий ребенок', 'Пассажир, летящий на отдых']

    # location = 'Дискотека'
    # roles = ['Диджей', 'Торговец наркотиками', 'Красивая глупая девушка',
    #          'Молодой красивый парень', 'Наркоман','Охранник', 'Бармен',
    #          'Отец красивой глупой девушки', 'Король танцпола']

    # location = 'Древняя Греция'
    # roles = ['Зевс','Одиссей','Прометей','Посейдон',
    #          'Геракл','Ахиллес', 'Орфей']

    # location = 'Магазин игрушек'
    # roles = ['Продавец', 'Покупатель', 'Ребёнок, который хочет игрушку',
    #          'Отец ребенка, который хочет игрушку', 'Игрушка йо-йо',
    #          'Игрушечная машинка', 'Игрушечная флейта']

    # location = 'Суд над маньяком'
    # roles = ['Судья', 'Маньяк', 'Адвокааааааат',
    #          'Друг маньяка, который его покрывает',
    #          'Муж убитой и изнасилованной девушки']

    # location = 'АВТОВАЗ'
    # roles = ['Работник завода', 'Конструктор Лады Калины',
    #          'Работник, пиздящий детали со склада',
    #          'Секретарша топ-менеджера', 'Лада Калина', 'Покупатель Лады']

    # location = 'Необитаемый остров, на который попал Робинзон'
    # roles = ['Робинзон', 'Каннибал с соседнего острова', 'Пятница',
    #          'Выращенная Робинзоном коза', 'Пират']

    # location = 'Заседание кафедры АТП накануне экзамена'
    # roles = ['Арсений Ашуха', 'Никита Пустовойтов', 'Виктор Кантор',
    #          'Иван Эрлих (умоляет, чтобы отчислили Перша)',
    #          'Никита Першуков (пришёл поныть)', 'Салыч']

    # location = 'Оружейный магазин'
    # roles = ['Продавец', 'Покупатель', 'Охраник', 'Подозрительный негр',
    #          'Уборщица']

    # location = 'Бассейн'
    # roles = ['Инструктор по плаванию', 'Утопленик', 'Беременная женщина',
    #          'Пловец', 'Ребенок, который учится плавать']

    # location = 'Фабрика Санта Клауса'
    # roles = ['Санта', 'Русский Дед Мороз (пришёл устранять конкурента)',
    #          'Фея леденцов', 'Гномик, заворачивающий подарки
    #          (или не гном, я хуй знает кто там у них,
    #           пусть блять гномик будет, гомик нахуй)',
    #          'Мальчик Саша, который пришёл на экскурсию']

    # location = 'Тюрячка!'
    # roles = ['Вор в законе', 'Петух', 'Кольщик', 'Смотрящий',
    #          'Старик, отбывающий пожизненное']

    # location = 'Кладбище'
    # roles = ['Труп', 'Алчный продавец памятников', 'Скорбящий родственник',
    #          'Смерть', 'Кладоискатель']

    names = []
    roles.append(spy)
    random.shuffle(roles)

    for role in roles:
        os.system('clear')
        print('Твоя роль: ', role)
        if role != spy:
            print('Локация: ', location)
        print('Введите имя игрока: ', end='')
        names.append(input())
    os.system('clear')

    print('Локация: ', location)
    for name, role in zip(names, roles):
        print('{} играет роль "{}"'.format(name, role))
    print('Первый вопрос задает {}'.format(random.choice(names)))
    print('Нажмите Enter, чтобы начать игру')
    input()
    current_time = time.strftime('%H:%M:%S',
                                 time.localtime(time.time()))
    print('Время начала игры {}'.format(current_time))
    all_time = 600
    for i in range(10):
        time.sleep(60)
        print('{} seconds left'.format(all_time - (i + 1) * 60))
    print('Игра окончена!')


if __name__ == '__main__':
    main()
