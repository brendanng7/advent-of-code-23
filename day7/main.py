file = open("/Users/brendanng/Documents/Code/advent-of-code-23/day7/data.txt", "r")
handbids = list(map(lambda x : x.split(" "), file.read().split("\n")))
for handbid in handbids:
    handbid[1] = int(handbid[1])

def printer(handbids):
    for handbid in handbids:
        print(handbid)

def card_strength(card):
    try:
        return int(card)
    except:
        obj ={
            "T" : 10,
            "J" : 11,
            "Q" : 12,
            "K" : 13,
            "A" : 14
        }
        return obj[card]


def hand_type(hand):
    pass
    obj = {}
    for card in hand:
        if card in obj:
            obj[card] += 1
        else:
            obj[card] = 1
    distinct_num = len(obj)
    highest_num = max(obj.values())
    
    if distinct_num == 1:
        return 7
    elif distinct_num == 2 and highest_num == 4:
        return 6
    elif distinct_num == 2 and highest_num == 3:
        return 5
    elif distinct_num == 3 and highest_num == 3:
        return 4
    elif distinct_num == 3 and highest_num == 2:
        return 3
    elif distinct_num == 4:
        return 2
    else:
        return 1

for handbid in handbids:
    hand = handbid[0]
    handbid.append(hand_type(hand))

def swap(a, b, arr):
    temp = arr[a]
    arr[a] = arr[b]
    arr[b] = temp

def f(hand1, hand2):
    for i in range(0, 5):
        str1 = card_strength(hand1[0][i])
        str2 = card_strength(hand2[0][i])
        if str1 == str2:
            continue
        elif str1 > str2:
            return True
        else:
            return False
obj = {}
print(obj["J"] if "J" in obj else 0)

# for i in range(len(handbids)):
#     for j in range(len(handbids) - i - 1):
#         if f(handbids[j], handbids[j + 1]):
#             swap(j, j + 1, handbids)
# handbids = sorted(handbids, key=lambda hand : hand[2], reverse=False)

# printer(handbids)

# sum = 0
# for i in range(len(handbids)):
#     hand = handbids[i]
#     sum += hand[1] * (i + 1)

# print(sum)




