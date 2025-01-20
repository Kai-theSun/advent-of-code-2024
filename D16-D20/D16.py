def get_input():
    with open("D16_input", "r") as file:
        lines = file.readlines()
        map_input = []
        for line in lines:
            line_lst = list(line.strip("\n"))
            map_input.append(line_lst)
        start_pos = []
        end_pos = []
        for i in range(len(map_input)):
            for j in range(len(map_input[i])):
                if map_input[i][j] == "S":
                    start_pos = [i, j]
                elif map_input[i][j] == "E":
                    end_pos = [i, j]
        return map_input, start_pos, end_pos

def move(map_input, current_pos, end_pos, scores, routes):
    if current_pos == end_pos:
        return routes
    directions = [[0,1],[1,0],[-1,0],[0,-1]]
    routes.append(current_pos)
    for direction in directions:
        next_pos = [current_pos[0] + direction[0], current_pos[1] + direction[1]]
        if map_input[next_pos[0]][next_pos[1]] == "#":
            continue
        routes = move(map_input, next_pos, end_pos, scores, routes)
        routes.pop()
    return routes

def part1(map_input, start_pos, end_pos):
    scores = [0, 0]
    # [current_score, max_score]
    routes = []
    routes = move(map_input, start_pos, end_pos, scores, routes)
    print(routes)

map_data, start_pos, end_pos = get_input()
#print(map_data, start_pos, end_pos)
part1(map_data, start_pos, end_pos)

