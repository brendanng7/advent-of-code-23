data = """Time:        54     94     65     92
Distance:   302   1476   1029   1404"""

filter1 = list(map(lambda x : x.split(" "),data.split("\n")))
for i in range(len(filter1)):
    filter1[i] = [int(value) for value in filter1[i] if value.isdigit()]
print(filter1)

def racing_methods(race_duration, dist_to_beat):
    number_of_ways = 0
    for speed in range(1, race_duration):
        if (speed * (race_duration - speed) > dist_to_beat):
            number_of_ways += 1
    return number_of_ways

multiplied = 1

for i in range(len(filter1[0])):
    time = filter1[0][i]
    dist = filter1[1][i]
    multiplied *= racing_methods(time, dist)

print(multiplied)

print(racing_methods(54946592, 302147610291404))