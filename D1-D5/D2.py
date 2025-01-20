def get_input():
    with open("D2_input", "r") as file:
        lines = file.readlines()
        arr = []
        for line in lines:
            x = (line.split(" "))
            for i in range(len(x)):
                x[i] = int(x[i])
            arr.append(x)
        return arr

def is_safe(x):
    is_increase = True if x[1] > x[0] else False
    res = True
    if is_increase:
        for i in range(1, len(x)):
            if x[i - 1] >= x[i] or (x[i] - x[i - 1]) > 3:
                res = False
                break
    elif not is_increase:
        for i in range(1, len(x)):
            if x[i - 1] <= x[i] or (x[i - 1] - x[i]) > 3:
                res = False
                break
    return res

def part1(arr):
    summary = 0
    for row in arr:
        if is_safe(row):
            summary += 1
    return summary

def part2(arr):
    summary = 0
    for row in arr:
        for i in range(len(row)):
            arr_d = row[:i] + row[i + 1:]
            if is_safe(arr_d):
                summary += 1
                break
    return summary

print(part1(get_input()), part2(get_input()))