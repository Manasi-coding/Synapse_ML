from itertools import combinations

pokedex = {
    "Pikachu": ("Electric", ),
    "Charizard": ("Fire", "Flying"),
    "Lapras": ("Water", "Ice"),
    "Machamp": ("Fighting",),
    "Mewtwo": ("Psychic", "Fighting"),
    "Hoopa": ("Psychic", "Ghost", "Dark"),
    "Lugia": ("Psychic", "Flying", "Water"),
    "Squirtle": ("Water",),
    "Gengar": ("Ghost", "Poison"),
    "Onix": ("Rock", "Ground")
}

c=3     # 3 pokemons
bestTeam = []
bestTypes = set()

for t in combinations(pokedex.keys(),c):
    types = set()
    for i in t:
        types.update(pokedex[i])
    if len(types) > len(bestTypes):
        bestTypes = types
        bestTeam = t

print(f"The Best Team is: {bestTeam}")