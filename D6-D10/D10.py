def get_input():
    with open("D10_input", "r") as file:
        input_map = []
        lines = file.readlines()
        for line in lines:
            input_map.append(list(line.strip("\n")))

        start_loc = []
        end_loc = []
        #{'idx':int, 'has_arrived':bool, 'location':[int,int]}
        idx_0, idx_9 = 0, 0
        for i in range(len(input_map)):
            for j in range(len(input_map[0])):
                if input_map[i][j] == ".":
                    continue
                else:
                    if input_map[i][j] == '0':
                        start_loc.append({"idx":idx_0, "arrived":False, "loc":[i,j]})
                        idx_0 += 1
                    elif input_map[i][j] == '9':
                        end_loc.append({"idx":idx_9, "arrived":False, "loc":[i,j]})
                    input_map[i][j] = int(input_map[i][j])
        return input_map, start_loc, end_loc

def try_move(input_map, current_loc, current_step, end_loc, total_score, is_part2):
    i = current_loc[0]
    j = current_loc[1]
    if current_step == 9:
        for loc in end_loc:
            if loc["loc"] == current_loc:
                if is_part2:
                    return total_score + 1
                if loc["arrived"]:
                    return total_score
                else:
                    loc["arrived"] = True
                    return total_score + 1
        return total_score

    #up
    if i > 0 and input_map[i-1][j] == current_step + 1:
        total_score = try_move(input_map, [i-1,j], current_step + 1, end_loc, total_score, is_part2)
    #down
    if i < len(input_map)-1 and input_map[i+1][j] == current_step + 1:
        total_score = try_move(input_map, [i+1,j], current_step + 1, end_loc, total_score, is_part2)
    #left
    if j > 0 and input_map[i][j-1] == current_step + 1:
        total_score = try_move(input_map, [i, j-1], current_step + 1, end_loc, total_score, is_part2)
    #right
    if j < len(input_map[0])-1 and input_map[i][j+1] == current_step + 1:
        total_score = try_move(input_map, [i, j+1], current_step + 1, end_loc, total_score, is_part2)
    return total_score

def part1(input_map, start_loc, end_loc):
    score = 0
    for start in start_loc:
        for i in end_loc:
            i["arrived"] = False
        current_score = try_move(input_map, start["loc"], 0, end_loc, 0, False)
        score += current_score
    return score

def part2(input_map, start_loc, end_loc):
    score = 0
    for start in start_loc:
        current_score = try_move(input_map, start["loc"], 0, end_loc, 0, True)
        score += current_score
    return score

input_map, start_loc, end_loc = get_input()
print(part2(input_map, start_loc, end_loc))