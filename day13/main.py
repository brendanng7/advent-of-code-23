file = open('advent-of-code-23/day13/data.txt', 'r')
filter1 = file.read().split('\n\n')
filter1 = [grid.splitlines() for grid in filter1]

def tolerant(above, below):

    return sum(sum(1 if a != b else 0 for a,b in zip(r1, r2)) for r1, r2 in zip(above, below)) == 1
    # num_of_differences = sum(1 for a, b in zip(above, below) if a != b)

def find_mirror(grid):
    for r in range(1, len(grid)):
        above = grid[:r][::-1]
        below = grid[r:]

        above = above[:len(below)]
        below = below[:len(above)]

        if tolerant(above, below):
            return r
        
    return 0
total = 0
for grid in filter1:
    total += find_mirror(grid) * 100

    transposed = list(zip(*grid))
    total += find_mirror(transposed)

print(total)