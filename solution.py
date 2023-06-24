from typing import List

# Put your solution in the solution()-function
import json

def solution() -> List[str]:
    # JSONデータの読み込み
    with open('pokemon_data.json','r',encoding="utf-8") as file:
        pokemon_data = json.load(file)

    # 1,2,3の条件に合うデータを抽出する
    filtered_pokemon_data = []
    for item in pokemon_data:
        if 'くさ' in item['types'] and item['stats']['hp'] >= 80 and (len(item['abilities']) + len(item['hiddenAbilities'])) >= 3:
            filtered_pokemon_data.append(item)

    # フィルタしたデータを'name'カラムを取り出し、昇順で並び変える
    name_column = [d.get('name') for d in filtered_pokemon_data]
    name_column.sort()

    return name_column