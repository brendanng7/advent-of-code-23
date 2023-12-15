file = open('advent-of-code-23/day11/data.txt', 'r')
filter1 = file.read().split('\n')

arr1 = []
for i in range(len(filter1)):
    row = filter1[i]
    if row.find('#') == -1:
        arr1.append(i)
# for i in range(len(arr1)):
#     index = arr1[i]
#     filter1.insert(index + i, '.' * len(filter1[0]))

arr2 = []
for i in range(len(filter1[0])):
    col = [filter1[j][i] for j in range(len(filter1))]
    if '#' not in col:
        arr2.append(i)
# for i in range(len(arr2)):
#     index = arr2[i]
#     for j in range(len(filter1)):
#         row = filter1[j]
#         filter1[j] = row[:index + i] + '.' + row[index + i:]

arr3 = []
for r in range(len(filter1)):
    row = filter1[r]
    arr = list(filter(lambda x : x != None, [[r, c] if row[c] == '#' else None for c in range(len(filter1[r]))]))
    arr3.extend(arr) if arr != [] else 0
    
sum = 0
for i in range(len(arr3)):
    firstx = arr3[i][0]
    firsty = arr3[i][1]
    for j in range(i + 1, len(arr3)):
        secondx = arr3[j][0]
        secondy = arr3[j][1]
        ax = max(firstx, secondx); bx = min(firstx, secondx)
        ay = max(firsty, secondy); by = min(firsty, secondy)
        arr4 = list(filter(lambda x : bx < x < ax, arr1))
        arr5 = list(filter(lambda y : by < y < ay, arr2))
        print(arr4, arr5)


        sum += (ax - bx) + len(arr4) * 999999 if len(arr4) != 0 else ax - bx
        sum += (ay - by) + len(arr5) * 999999 if len(arr5) != 0 else ay - by

print(sum)



