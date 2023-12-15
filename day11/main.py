file = open('advent-of-code-23/day11/data.txt', 'r')
filter1 = file.read().split('\n')

arr1 = []
for i in range(len(filter1)):
    row = filter1[i]
    if row.find('#') == -1:
        arr1.append(i)
for i in range(len(arr1)):
    index = arr1[i]
    filter1.insert(index + i, '.' * len(filter1[0]))

arr2 = []
for i in range(len(filter1[0])):
    col = [filter1[j][i] for j in range(len(filter1))]
    if '#' not in col:
        arr2.append(i)
for i in range(len(arr2)):
    index = arr2[i]
    for j in range(len(filter1)):
        row = filter1[j]
        filter1[j] = row[:index + i] + '.' + row[index + i:]

arr3 = []
for r in range(len(filter1)):
    row = filter1[r]
    arr = list(filter(lambda x : x != None, [[r, c] if row[c] == '#' else None for c in range(len(filter1[r]))]))
    arr3.extend(arr) if arr != [] else 0
    

sum = 0
for i in range(len(arr3)):
    first_coord = arr3[i]
    for j in range(i + 1, len(arr3)):
        second_coord = arr3[j]
        sum += abs(first_coord[0] - second_coord[0])
        sum += abs(first_coord[1] - second_coord[1])
print(arr3)
print(sum)



