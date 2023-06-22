    # Exercise: Process JSON-file

## Prerequisites

- Poetry
- Python 3

## Setup

1. Clone the repository.
1. Run this in the repository folder: `poetry install`

## About the data-file

The data is in file `pokemon_data.json`. The file contains information about ポケモン. For each Pokemon, the following information is necessary for this exercise:

- `no`: Number of the Pokemon
- `name`: Name of the Pokemon
- `types`: List of types of the Pokemon (like grass, poison etc.)
- `abilities` & `hiddenAbilities`: List of abilities the Pokemon can use.
- `stats`: A dictionary containing stats like HP, attack, defence etc.

## Exercise

1. Read the given dataset `pokemon_data.json`
1. Extract the Pokemon, that satisfy **ALL** of the following:
    1. Has くさ type
    1. Has `80` or more health points
    1. Has **3 or more** abilities (also counting hidden ones!)
1. Return the names of these Pokemons as a `list` or strings, sorted by lexicographical (あいうえお) order.

## Submitting your solution

1. Put your solution into the function `solution()` in `solution.py`. You can also add other functions in addition, if you need. Your `solution()`-function needs to return the list of Pokemon-names.
1. Verify that it works by executing `poetry run python verify.py`.
1. If it works, create a new branch and push to this branch.
1. Ask Moritz for feedback on your code.

If you have trouble, ask your colleagues for help and work together! Group submissions are allowed & encouraged. :)
