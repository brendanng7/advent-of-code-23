from math import lcm

file = open("advent-of-code-23/day8/data.txt", "r")
filter = file.read().split("\n")

instructions = filter[0]

nodeList = {
    node[:3] : [node[7: 10], node[12: 15]] for node in filter[2::] 
}

currNodes = [node for node in list(nodeList.keys()) if node[2] == "A"]

counter = 0
i = 0
for j in range(len(currNodes)):
    currNode = currNodes[j]
    while currNode[2] != "Z":
        instruction = instructions[i]; i = i + 1 if i < len(instructions) - 1 else 0
        currNode = nodeList[currNode][0] if instruction == "L" else nodeList[currNode][1]
        counter += 1    
        print(counter, currNodes, instruction) 
    currNodes[j] = counter
    counter = 0
    i = 0
print(currNodes)

print(lcm(17141, 16579, 18827, 12083, 13207, 22199))
