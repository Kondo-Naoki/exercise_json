from typing import List

# Put your solution in the solution()-function
import json

def solution() -> List[str]:

    # condition1
    def typefilter() -> bool:
        return d["types"] == "くさ"

    # conditon2
    def helthpointhigher() -> bool:
        return d["stats"]["hp"] >= 80

    # conditon3
    def abilitysum() -> bool:
       return len(d["abilities"]) >= 3

    # File load
    f = open('pokemon_data.json', 'r',encoding="utf-8")
    pokemonLists = json.load(f)
    #print('pokemonLists:{}'.format(type(pokemonLists)))

    d = pokemonLists

    # Extract condiion 1,2,3
    filter(typefilter,d)
    filter(helthpointhigher,d)
    filter(abilitysum,d)   

    # Sort
    l_name = [l.get('name') for l in d]

    return l_name