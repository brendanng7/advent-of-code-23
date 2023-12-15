file = open("advent-of-code-23/day8/data.txt", "r")
filter = file.read().split("\n")

# print(filter)
instructions = filter[0]
print(instructions)

nodeList = {
    node[:3] : [node[7: 10], node[12: 15]] for node in filter[2::] 
}
print(nodeList)

lastNode = "ZZZ"
currNode = "AAA"
counter = 0
i = 0
while currNode != lastNode:
    instruction = instructions[i]; i = i + 1 if i < len(instructions) - 1 else 0
    currNode = nodeList[currNode][0] if instruction == "L" else nodeList[currNode][1]; counter += 1
print(counter)