# from typing import List

# # Put your solution in the solution()-function
# import json

# result = {}

# def solution() -> List[str]:

#     # condition1
#     def typefilter() -> bool:
#         return 'くさ' in result['types'] 

#     # conditon2
#     def helthpointhigher() -> bool:
#         return result["stats"]["hp"] >= 80

#     # conditon3
#     def abilitysum() -> bool:
#        return len(result["abilities"]) >= 3

#     # File load
#     f = open('pokemon_data.json', 'r',encoding="utf-8")
#     pokemonLists = json.load(f)
#     #print('pokemonLists:{}'.format(type(pokemonLists)))

#     result = pokemonLists

#     # Extract condiion 1,2,3
#     result = filter(typefilter,result)    
#     result = filter(helthpointhigher,result)
#     result = filter(abilitysum,result)   

#     # Sort
#     l_name = [l.get('name') for l in result]

#     return l_name



from typing import List

# Put your solution in the solution()-function
import json

def filter_json_by_column(json_data):
    filtered_items = []
    for item in json_data:
        if 'くさ' in item['types'] and item['stats']['hp'] >= 80 and (len(item['abilities']) + len(item['hiddenAbilities'])) >= 3:
            filtered_items.append(item)
    return filtered_items

def solution() -> List[str]:
    # JSONデータの読み込み
    with open('pokemon_data.json','r',encoding="utf-8") as file:
        json_data = json.load(file)

    # 条件に合うデータを抽出する
    keys = filter_json_by_column(json_data)
    name_column = [d.get('name') for d in keys]

    # 抽出したデータを、名前で昇順で並び変える
    name_column.sort()

    return name_column