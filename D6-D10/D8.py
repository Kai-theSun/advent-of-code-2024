input_data = []
nodes = {}
#{"c":[[i1,j1],[i2,j2]]}
with open("D8_input", "r") as file:
    lines = file.readlines()
    for i in range(len(lines)):
        line = list(lines[i].strip("\n"))
        input_data.append(line)

for i in range(len(input_data)):
    for j in range(len(input_data[i])):
        if input_data[i][j] == '.':
            continue
        if input_data[i][j] in nodes:
            nodes[input_data[i][j]].append([i, j])
        else:
            nodes.update({input_data[i][j]: [[i, j]]})

result = []
for i in range(len(input_data)):
    result.append([0] * len(input_data[i]))

def find_anti(node, data):
    total = 0
    for i in range(len(node) - 1):
        x1 = node[i][0]
        y1 = node[i][1]
        for j in range(i + 1, len(node)):
            x2 = node[j][0]
            y2 = node[j][1]
            dx = x2 - x1
            dy = y2 - y1
            if (0 <= x2 + dx < len(data[0])) and (0 <= y2 + dy < len(data)):
                result[x2 + dx][y2 + dy] = 1
                total += 1
            if (0 <= x1 - dx < len(data[0])) and (0 <= y1 - dy < len(data)):
                result[x1 - dx][y1 - dy] = 1
                total += 1
    return total

def find_anti4part2(node, data):
    for i in range(len(node) - 1):
        x1 = node[i][0]
        y1 = node[i][1]
        for j in range(i + 1, len(node)):
            x2 = node[j][0]
            y2 = node[j][1]
            dx = x2 - x1
            dy = y2 - y1
            k = 0
            while (0 <= x2 + dx * k < len(data[0])) and (0 <= y2 + dy * k < len(data)):
                result[x2 + dx * k][y2 + dy * k] = 1
                k += 1
            k = 0
            while (0 <= x1 - dx * k < len(data[0])) and (0 <= y1 - dy * k < len(data)):
                result[x1 - dx * k][y1 - dy * k] = 1
                k += 1
    return

def part1(nodes, data):
    node_num = 0
    total_num = 0
    for key,value in nodes.items():
        total_num += find_anti(value, data)

    for i in range(len(result)):
        for j in range(len(result[i])):
            if result[i][j] == 1:
                node_num += 1
    return node_num

def part2(nodes, data):
    node_num = 0
    for key, value in nodes.items():
        find_anti4part2(value, data)

    for i in range(len(result)):
        for j in range(len(result[i])):
            if result[i][j] == 1:
                node_num += 1
    return node_num

print(part2(nodes, input_data))