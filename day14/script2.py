#looking_for = [5,1,5,8,9]
looking_for = [5,5,4,4,0,1]

recipes = [3, 7]
elf1 = 0
elf2 = 1

while True:
    new_recipe = recipes[elf1] + recipes[elf2]
    recipes.extend(int(x) for x in list(str(new_recipe)))
    elf1 = (elf1 + recipes[elf1] + 1) % len(recipes)
    elf2 = (elf2 + recipes[elf2] + 1) % len(recipes)
    #print(recipes)

    if len(recipes) > len(looking_for):
        
        if recipes[-len(looking_for):] == looking_for:
            print('part2', len(recipes) - len(looking_for))
            break
        if recipes[-len(looking_for)-1:-1] == looking_for:
            print('part2', len(recipes) - len(looking_for) - 1)
            break
