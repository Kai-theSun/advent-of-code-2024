input_data = []
position = {"i":0, "j":0, "forward":""}
with open("D6_input", "r")as file:
    lines = file.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].strip("\n")
        row = []
        for j in range(len(lines[0])):
            if lines[i][j] == ".":
                row.append({"is_barrel":False, "has_visit":False, "potential_block": False})
            elif lines[i][j] == "#":
                row.append({"is_barrel":True, "has_visit":False, "potential_block": False})
            elif lines[i][j] == "v":
                row.append({"is_barrel":False, "has_visit":True, "potential_block": False})
                position["i"] = i
                position["j"] = j
                position["forward"] = "down"
            elif lines[i][j] == ">":
                row.append({"is_barrel":False, "has_visit":True, "potential_block": False})
                position["i"] = i
                position["j"] = j
                position["forward"] = "right"
            elif lines[i][j] == "<":
                row.append({"is_barrel":False, "has_visit":True, "potential_block": False})
                position["i"] = i
                position["j"] = j
                position["forward"] = "left"
            elif lines[i][j] == "^":
                row.append({"is_barrel":False, "has_visit":True, "potential_block": False})
                position["i"] = i
                position["j"] = j
                position["forward"] = "up"
        input_data.append(row)

def move(data):
    i = position["i"]
    j = position["j"]
    match position["forward"]:
        case "down":
            if i >= len(data) - 1:
                return -1
            if data[i+1][j]["is_barrel"]:
                position["forward"] = "left"
                return 0
            else:
                position["i"] = i + 1
                data[i+1][j]["has_visit"] = True
                return 1
        case "right":
            if j >= len(data[0]) - 1:
                return -1
            if data[i][j+1]["is_barrel"]:
                position["forward"] = "down"
                return 0
            else:
                position["j"] = j + 1
                data[i][j+1]["has_visit"] = True
                return 1
        case "left":
            if j <= 0:
                return -1
            if data[i][j-1]["is_barrel"]:
                position["forward"] = "up"
                return 0
            else:
                position["j"] = j - 1
                data[i][j-1]["has_visit"] = True
                return 1
        case "up":
            if i <= 0:
                return -1
            if data[i-1][j]["is_barrel"]:
                position["forward"] = "right"
                return 0
            else:
                position["i"] = i - 1
                data[i-1][j]["has_visit"] = True
                return 1

def part1():
    visit_num = 0
    turning_num = 0
    while True:
        print(position)
        res = move(input_data)
        if res == -1:
            break
        elif res == 0:
            turning_num += 1
    for i in range(len(input_data)):
        for j in range(len(input_data[0])):
            if input_data[i][j]["has_visit"]:
                visit_num += 1
    return visit_num, turning_num

def part2():
    potential_blocks = 0
    initial_position = position.copy()
    print(initial_position)
    for i in range(len(input_data)):
        for j in range(len(input_data[i])):
            if input_data[i][j]["is_barrel"]:
                continue
            if i == initial_position["i"] and j == initial_position["j"]:
                continue
            position_history = [tuple([initial_position["i"], initial_position["j"], initial_position["forward"]])]
            position["i"] = initial_position["i"]
            position["j"] = initial_position["j"]
            position["forward"] = initial_position["forward"]
            input_data[i][j]["is_barrel"] = True
            while True:
                res = move(input_data)
                if res == -1:
                    break
                elif res == 0:
                    temp_i = position["i"]
                    temp_j = position["j"]
                    temp_forward = position["forward"]
                    temp_position = tuple([temp_i, temp_j, temp_forward])
                    if temp_position in position_history:
                        input_data[i][j]["potential_block"] = True
                        break
                    else:
                        position_history.append(tuple([temp_i, temp_j, temp_forward]))
            input_data[i][j]["is_barrel"] = False
        print(f"finish[{i}]")
    for i in range(len(input_data)):
        for j in range(len(input_data[i])):
            if input_data[i][j]["potential_block"]:
                potential_blocks += 1
    return potential_blocks

print(part2())
