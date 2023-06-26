from typing import List

# Put your solution in the solution()-function
import json

#Search Conditon
pokemon_type = 'くさ'
min_hp = 80
min_abilities = 3

def solution() -> List[str]:

    # JSONデータの読み込み
    with open('pokemon_data.json','r',encoding="utf-8") as file:
        pokemon_list = json.load(file)

    # # 1,2,3の条件に合うポケモンを抽出する
    filtered_pokemon_name = [item['name'] for item in pokemon_list \
        if pokemon_type in item['types'] and \
            item['stats']['hp'] >= min_hp and \
            (len(item['abilities']) + len(item['hiddenAbilities'])) >= min_abilities]

    # # 抽出したデータを名前で昇順に並び変える
    filtered_pokemon_name.sort()

    return filtered_pokemon_name