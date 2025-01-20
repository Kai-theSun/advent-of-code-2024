def get_input():
    with open("D12_input", "r") as file:
        input = []
        lines = file.readlines()
        for line in lines:
            input.append(list(line.strip("\n")))
        garden = []
        for i in range(len(input)):
            row = []
            for j in range(len(input[i])):
                row.append([input[i][j], False])
            garden.append(row)
        return garden

def find_group(i, j, char, map, arr):
    arr.append([i,j])
    map[i][j][1] = True

    if j-1 >= 0 and map[i][j-1][0] == char and not map[i][j-1][1]:
        arr = find_group(i, j-1, char, map, arr)
    if j+1 < len(map[0]) and map[i][j+1][0] == char and not map[i][j+1][1]:
        arr = find_group(i, j+1, char, map, arr)
    if i-1 >= 0 and map[i-1][j][0] == char and not map[i-1][j][1]:
        arr = find_group(i-1, j, char, map, arr)
    if i+1 < len(map) and map[i+1][j][0] == char and not map[i+1][j][1]:
        arr = find_group(i+1, j, char, map, arr)
    return arr

def calculate(char, arr, map):
    S = len(arr)
    C = 0
    for i in range(len(arr)):
        length = 4
        x = arr[i][0]
        y = arr[i][1]
        if y+1 < len(map) and map[x][y+1][0] == char:
            length -= 1
        if y-1 >= 0 and map[x][y-1][0] == char:
            length -= 1
        if x+1 < len(map[0]) and map[x+1][y][0] == char:
            length -= 1
        if x-1 >= 0 and map[x-1][y][0] == char:
            length -= 1
        C += length
    return C * S

def calculate4part2(char, arr, map):
    S = len(arr)
    C = 0
    exist_col_r, exist_col_l = {}, {}
    exist_row_u, exist_row_d= {}, {}
    #{idx:[]}
    for i in range(len(arr)):
        x = arr[i][0]
        y = arr[i][1]
        if y+1 >= len(map) or map[x][y+1][0] != char:
            if y+1 in exist_col_r:
                exist_col_r[y+1].append(x)
            else:
                exist_col_r.update({y+1:[x]})
        if y-1 < 0 or map[x][y-1][0] != char:
            if y in exist_col_l:
                exist_col_l[y].append(x)
            else:
                exist_col_l.update({y:[x]})
        if x+1 >= len(map[0]) or map[x+1][y][0] != char:
            if x+1 in exist_row_u:
                exist_row_u[x+1].append(y)
            else:
                exist_row_u.update({x+1:[y]})
        if x-1 < 0 or map[x-1][y][0] != char:
            if x in exist_row_d:
                exist_row_d[x].append(y)
            else:
                exist_row_d.update({x: [y]})

    dics = [exist_col_r, exist_col_l, exist_row_d, exist_row_u]
    for dic in dics:
        for value in dic.values():
            value.sort()
            edges = 1
            for i in range(len(value)-1):
                if value[i+1] != value[i] + 1:
                    edges += 1
            C += edges
    print(char, C*S)
    return C * S

def solution(arr, is_part1):
    plants = {}
    #{"int": ("char",[[int,int]])}
    idx = 0
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j][1]:
                continue
            new_group = [arr[i][j][0], []]
            char = arr[i][j][0]
            new_group[1] = find_group(i, j, char, arr, new_group[1])
            plants.update({idx: new_group})
            idx+=1

    total = 0
    for key, value in plants.items():
        print(value)
        char = value[0]
        loc = value[1]
        if is_part1:
            total += calculate(char, loc, arr)
        else:
            total += calculate4part2(char, loc, arr)
    return total

print(solution(get_input(), False))