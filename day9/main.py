file = open("advent-of-code-23/day9/data.txt", "r")
filter = file.read().split("\n")
filter = list(map(lambda seq : list(map(lambda num: int(num), seq.split(" "))), filter))

print(filter)

def extrapolate(sequence):
    if (all(map(lambda x : x == 0, sequence))):
        return 0
    else:
        next_sequence = [sequence[i + 1] - sequence[i] for i in range(len(sequence) - 1)]
        next_value = extrapolate(next_sequence)
        return sequence[len(sequence) - 1] + next_value


sum = 0
for seq in filter:
    sum += extrapolate(seq)
print(sum)