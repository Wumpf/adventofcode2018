recipeoffset = 9
#recipeoffset = 554401

recipes = [3, 7]
elf1 = 0
elf2 = 1

while len(recipes) < recipeoffset + 10:
    new_recipe = recipes[elf1] + recipes[elf2]
    recipes.extend(int(x) for x in list(str(new_recipe)))
    elf1 = (elf1 + recipes[elf1] + 1) % len(recipes)
    elf2 = (elf2 + recipes[elf2] + 1) % len(recipes)
    #print(recipes)

print('part1', ''.join(str(x) for x in recipes[recipeoffset:(recipeoffset+10)]) )
