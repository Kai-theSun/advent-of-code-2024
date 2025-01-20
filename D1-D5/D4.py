def get_input():
    input_data = []
    with open("D4_input", "r") as file:
        lines = file.readlines()
        for line in lines:
            input_data.append(line.strip('\n'))
    return input_data

def find_from_arr(arr):
    res = 0
    for i in range(len(arr) - 3):
        if arr[i:i+4] == "XMAS" or arr[i:i+4] == "SAMX":
            res += 1
    return res

def part1(matrix):
    res = 0
    for row in matrix:
        res += find_from_arr(''.join(row))

    col = ''
    for j in range(len(matrix[0])):
        for i in range(len(matrix)):
            col += matrix[i][j]
        res += find_from_arr(col)
        col = ''

    # in 4 different dialog directions
    diag = ''
    for i in range(len(matrix)-1):
        temp_i = i
        j = 0
        while temp_i >= 0 and j < len(matrix[0]):
            diag += matrix[temp_i][j]
            temp_i -= 1
            j += 1
        res += find_from_arr(diag)
        diag = ''

    for j in range(len(matrix[0])):
        temp_j = j
        i = len(matrix) - 1
        while temp_j < len(matrix[0]) and i >= 0:
            diag += matrix[i][temp_j]
            i -= 1
            temp_j += 1
        res += find_from_arr(diag)
        diag = ''

    for i in range(1,len(matrix)):
        temp_i = i
        j = 0
        while temp_i < len(matrix) and j < len(matrix[0]):
            diag += matrix[temp_i][j]
            temp_i += 1
            j += 1
        res += find_from_arr(diag)
        diag = ''

    for j in range(len(matrix[0])):
        temp_j = j
        i = 0
        while temp_j < len(matrix[0]) and i < len(matrix):
            diag += matrix[i][temp_j]
            temp_j += 1
            i += 1
        res += find_from_arr(diag)
        diag = ''
    return res

def part2(matrix):
    res = 0
    for i in range(2, len(matrix)):
        for j in range(len(matrix[0]) - 2):
            arr1 = matrix[i][j] + matrix[i-1][j+1] + matrix[i-2][j+2]
            arr2 = matrix[i-2][j] + matrix[i-1][j+1] + matrix[i][j+2]
            if (arr1 == "MAS" or arr1 == "SAM") and (arr2 == "MAS" or arr2 == "SAM"):
                res += 1
    return res

print(part1(get_input()))
print(part2(get_input()))