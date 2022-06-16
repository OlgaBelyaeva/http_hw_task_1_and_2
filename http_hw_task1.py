# Работа с библиотекой requests, http-запросы
# Задача 1

import requests

def moste_intelligense(heroes):
    url = 'https://superheroapi.com/api/2619421814940190/search/'
    heroes_list = []
    for hero in heroes:
        response = requests.get(url + hero)
        heroes_list.append()#тут в скобках, должен быть код, который у героя из json достает значение intelligence
    moste_intelligense_hero = max(heroes_list, key=lambda x: int(x[1]))
    print(f'Самый умный герой - {moste_intelligense_hero})

moste_intelligense(['Hulk', 'Captain America', 'Thanos'])
