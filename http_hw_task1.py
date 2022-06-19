# Работа с библиотекой requests, http-запросы
# Задача 1 Кто самый умный супергерой?
# Решение на основе https://akabab.github.io/superhero-api/api/

import requests

def most_intelligence_hero(heroes):
    url = 'https://akabab.github.io/superhero-api/api/all.json'
    heroes_list = []
    response = requests.get(url)
    for i in response.json():
        if i['name'] in heroes:
            heroes_list.append((i['name'], i['powerstats']['intelligence']))
    moste_intelligense_hero = max(heroes_list, key=lambda x: int(x[1]))
    print(f'Самый умный супергерой {moste_intelligense_hero[0]}, его intelligence = {moste_intelligense_hero[1]}')

most_intelligence_hero(['Hulk', 'Captain America', 'Thanos'])


