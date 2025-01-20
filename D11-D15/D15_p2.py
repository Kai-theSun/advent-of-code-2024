def get_input():
    with open("D15_input", "r") as file:
        lines = file.readlines()
        idx = 0
        map_input= []
        while lines[idx] != "\n":
            line = lines[idx].strip("\n")
            map_line = []
            for i in range(len(line)):
                if line[i] == '#':
                    map_line.extend(['#', '#'])
                elif line[i] == '.':
                    map_line.extend(['.', '.'])
                elif line[i] == 'O':
                    map_line.extend(['[', ']'])
                elif line[i] == '@':
                    map_line.extend(['@', '.'])
            map_input.append(map_line)
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

def push_multi_boxes(map_data, current_position, direction, all_boxes, front_boxes):
    for pos in front_boxes:
        if pos not in all_boxes:
            all_boxes.append(pos)
    for pos in all_boxes:
        map_data[pos[0]][pos[1]] = "."
        map_data[pos[0]][pos[1] + 1] = "."
    for pos in all_boxes:
        map_data[pos[0] + direction[0]][pos[1]] = "["
        map_data[pos[0] + direction[0]][pos[1] + 1] = "]"
    map_data[current_position[0]][current_position[1]] = "."
    new_position = [current_position[0] + direction[0], current_position[1] + direction[1]]
    map_data[new_position[0]][new_position[1]] = "@"
    if map_data[new_position[0]][new_position[1] - 1] == "[":
        map_data[new_position[0]][new_position[1] - 1] = "."
    elif map_data[new_position[0]][new_position[1] + 1] == "]":
        map_data[new_position[0]][new_position[1] + 1] = "."
    return new_position

def find_boxes(map_data, current_position, direction, all_boxes, front_boxes):
    destination = [current_position[0] + direction[0], current_position[1] + direction[1]]
    moveable = False
    # initialize the first box's position
    if map_data[destination[0]][destination[1]] == "[":
        front_boxes.append([destination[0], destination[1]])
    elif map_data[destination[0]][destination[1]] == "]":
        front_boxes.append([destination[0], destination[1] - 1])
    while True:
        new_front = []
        moveable = True
        for pos in front_boxes:
            pos_i = pos[0]
            pos_j = pos[1]
            if map_data[pos_i + direction[0]][pos_j + direction[1]] == "#" or map_data[pos_i + direction[0]][pos_j + direction[1] + 1] == "#":
                moveable = False
                return all_boxes, front_boxes, moveable
            if map_data[pos_i + direction[0]][pos_j + direction[1]] == "." and map_data[pos_i + direction[0]][pos_j + direction[1] + 1] == ".":
                new_front.append(pos)
                continue
            # deal with left up position
            if map_data[pos_i + direction[0]][pos_j + direction[1]] == "[":
                moveable = False
                all_boxes.append(pos)
                new_front.append([pos_i + direction[0], pos_j + direction[1]])
            elif map_data[pos_i + direction[0]][pos_j + direction[1]] == "]":
                moveable = False
                all_boxes.append(pos)
                new_front.append([pos_i + direction[0], pos_j + direction[1] - 1])
            # deal with right up position
            if map_data[pos_i + direction[0]][pos_j + direction[1] + 1] == "[":
                moveable = False
                all_boxes.append(pos)
                new_front.append([pos_i + direction[0], pos_j + direction[1] + 1])
            # situation of right up ']' has been discussed in left up '['
        front_boxes = new_front
        if moveable:
            break
    return all_boxes, front_boxes, moveable

def push_boxes(map_data, current_position, direction):
    destination = [current_position[0] + direction[0], current_position[1] + direction[1]]
    # lift/right pushing is easier, only need to deal with one line
    if direction == [0, 1] or direction == [0, -1]:
        while 0 <= destination[0] < len(map_data) and 0 <= destination[1] < len(map_data[0]):
            if map_data[destination[0]][destination[1]] == "[" or map_data[destination[0]][destination[1]] == "]":
                destination[0] += direction[0]
                destination[1] += direction[1]
                continue
            # meeting a '#' means these boxes are not moveable due to wall
            elif map_data[destination[0]][destination[1]] == "#":
                return current_position
            elif map_data[destination[0]][destination[1]] == ".":
                map_data[current_position[0]][current_position[1]] = "."
                current_position = [current_position[0] + direction[0], current_position[1] + direction[1]]
                map_data[current_position[0]][current_position[1]] = "@"
                for i in range(current_position[1], destination[1], direction[1]):
                    if map_data[destination[0]][i] == "[":
                        map_data[destination[0]][i] = "]"
                    elif map_data[destination[0]][i] == "]":
                        map_data[destination[0]][i] = "["
                # push right
                if direction == [0, 1]:
                    map_data[destination[0]][destination[1]] = "]"
                # push left
                elif direction == [0, -1]:
                    map_data[destination[0]][destination[1]] = "["
                return current_position
        return current_position
    # push up/down is complex, need to find all the adjacent boxes
    elif direction == [1, 0] or direction == [-1, 0]:
        all_boxes, front_boxes = [], []
        all_boxes, front_boxes, moveable = find_boxes(map_data, current_position, direction, all_boxes, front_boxes)
        if not moveable:
            return current_position
        else:
            return push_multi_boxes(map_data, current_position, direction, all_boxes, front_boxes)

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
    elif map_data[destination[0]][destination[1]] == "[" or map_data[destination[0]][destination[1]] == "]":
        return push_boxes(map_data, current_position, direction)
    return current_position

def part2(map_data, move_data, init_position):
    idx = 0
    current_position = [init_position[0], init_position[1]]
    show_map(map_data)
    while idx < len(move_data):
        #input(f"next is {move_data[idx]}\n")
        current_position = move(map_data, current_position, move_data[idx])
        #show_map(map_data)
        idx += 1
    show_map(map_data)
    res = 0
    for i in range(len(map_data)):
        for j in range(len(map_data[i])):
            if map_data[i][j] == "[":
                res += i * 100 + j
    return res

def show_map(map_data):
    for line in map_data:
        string = ""
        for char in line:
            string += char
        print(string)

map_input, move_input, initial_position = get_input()
print(part2(map_input, move_input, initial_position))