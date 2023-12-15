file = open("advent-of-code-23/day10/data.txt", 'r')
instructions = file.read().split("\n")
# finding the coordinates of starting position

starting_coord = [0, 0]
for r in range(len(instructions)):
    row = instructions[r]
    if "S" in row:
        c = row.find("S")
        starting_coord = [r, c]

coords = [[0 for cols in range(len(instructions[0]))] for rows in range(len(instructions))]
coords[starting_coord[0]][starting_coord[1]] = 1
current_coord = starting_coord


def find_connecting(C):
    r = C[0]
    c = C[1]
    connected = []
    possibles = list(filter(lambda x : x != None, [
                [r - 1, c, ['|','7','F','S']] if r > 0 and instructions[r][c] in ['|','L','J','S'] else None,
                [r, c - 1, ['-','L','F','S']] if c > 0 and instructions[r][c] in ['-','J','7','S'] else None,
                [r, c + 1, ['-','J','7','S']] if c < len(coords[0]) - 1 and instructions[r][c] in ['-','L','F','S'] else None,
                [r + 1, c, ['|','L','J','S']] if r < len(coords) - 1 and instructions[r][c] in ['|','F','7','S'] else None,
                ]))

    for possible in possibles:
        r = possible[0]
        c = possible[1]
        loopable = possible[2]
        if instructions[r][c] in loopable:
            tile = instructions[r][c]
            connected.append([r, c])
    return connected

last_coord = find_connecting(starting_coord)[0]

count = 1
current_coord = find_connecting(starting_coord)[1]
coords[current_coord[0]][current_coord[1]] = 1
# print('\n'.join(' '.join(str(x) for x in row) for row in coords))
while current_coord != last_coord:
    connected = find_connecting(current_coord)
    first = connected[0]
    second = connected[1]
    if coords[first[0]][first[1]] == 1:
        current_coord = second
        coords[current_coord[0]][current_coord[1]] = 1
    else:
        current_coord = first
        coords[current_coord[0]][current_coord[1]] = 1
    count += 1
    # print('\n'.join(' '.join(str(x) for x in row) for row in coords))


# print('\n'.join(' '.join(str(x) for x in row) for row in coords))
print((count + 1)/2)
