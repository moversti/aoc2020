file = open("input.txt", "r")
rivit = file.read().splitlines()

right = 3
down = 1
pos_x = 0
pos_y = 0
width = len(rivit[0])
height = len(rivit)

trees = 0
while pos_y < height:
    if rivit[pos_y][pos_x % width] == '#':
        trees = trees + 1
    pos_x = pos_x + right
    pos_y = pos_y + down
print(trees)

rules = ((1, 1), (3, 1), (5, 1), (7, 1), (1, 2))

width = len(rivit[0])
height = len(rivit)

trees_mul = 1
for rule in rules:
    trees = 0
    pos_x = 0
    pos_y = 0
    while pos_y < height:
        if rivit[pos_y][pos_x % width] == '#':
            trees = trees + 1
        pos_x = pos_x + rule[0]
        pos_y = pos_y + rule[1]
    trees_mul = trees_mul * trees
print(trees_mul)
