def get_input():
    with open("D15_input", "r") as file:
        lines = file.readlines()
        idx = 0
        map_input= []
        while lines[idx] != "\n":
            line = lines[idx].strip("\n")
            map_input.append(list(line))
            idx += 1
        idx += 1
        move_input = []
        while idx < len(lines):
            line = lines[idx].strip("\n")
            move_input.extend(list(line))
            idx += 1
        for i in range(len(map_input)):
            for j in range(len(map_input[i])):
                if map_input[i][j] == "@":
                    initial = [i, j]
                    return map_input, move_input, initial

def push_boxes(map_data, current_position, direction):
    destination = [current_position[0] + direction[0], current_position[1] + direction[1]]
    while 0 <= destination[0] < len(map_data) and 0 <= destination[1] < len(map_data[0]):
        if map_data[destination[0]][destination[1]] == "O":
            destination[0] += direction[0]
            destination[1] += direction[1]
            continue
        elif map_data[destination[0]][destination[1]] == "#":
            return current_position
        elif map_data[destination[0]][destination[1]] == ".":
            map_data[destination[0]][destination[1]] = "O"
            map_data[current_position[0]][current_position[1]] = "."
            current_position = [current_position[0] + direction[0], current_position[1] + direction[1]]
            map_data[current_position[0]][current_position[1]] = "@"
            return current_position
    return current_position

def move(map_data, current_position, operation):
    current_i, current_j = current_position[0], current_position[1]
    direction = []
    match operation:
        case "<":
            direction = [0, -1]
        case ">":
            direction = [0, 1]
        case "^":
            direction = [-1, 0]
        case "v":
            direction = [1, 0]
    destination = [current_i + direction[0], current_j + direction[1]]
    if destination[0] < 0 or destination[0] >= len(map_data) or destination[1] < 0 or destination[1] >= len(map_data[0]):
        return current_position
    if map_data[destination[0]][destination[1]] == "#":
        return current_position
    elif map_data[destination[0]][destination[1]] == ".":
        map_data[destination[0]][destination[1]] = "@"
        map_data[current_position[0]][current_position[1]] = "."
        return destination
    elif map_data[destination[0]][destination[1]] == "O":
        return push_boxes(map_data, current_position, direction)


def part1(map_data, move_data, init_position):
    idx = 0
    current_position = [init_position[0], init_position[1]]
    while idx < len(move_data):
        current_position = move(map_data, current_position, move_data[idx])
        idx += 1
    res = 0
    for i in range(len(map_data)):
        for j in range(len(map_data[i])):
            if map_data[i][j] == "O":
                res += i * 100 + j
    return res

map_input, move_input, initial_position = get_input()
print(part1(map_input, move_input, initial_position))
