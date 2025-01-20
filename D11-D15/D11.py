def get_input():
    with open("D11_input", "r") as file:
        line = file.readline().strip("\n").split(" ")
        for i in range(len(line)):
            line[i] = int(line[i])
    return line
CHANGE_TIMES1 = 25
CHANGE_TIMES2 = 75

def blink(arr):
    idx = 0
    while idx < len(arr):
        if arr[idx] == 0:
            arr[idx] = 1
        elif len(str(arr[idx])) % 2 == 0:
            mid = len(str(arr[idx])) // 2
            left = int(str(arr[idx])[0:mid])
            right = int(str(arr[idx])[mid:])
            arr.insert(idx, left)
            idx += 1
            arr[idx] = right
        else:
            arr[idx] *= 2024
        idx += 1
    return arr

def part1(arr, it_times = CHANGE_TIMES1):
    times = 0
    while times < it_times:
        arr = blink(arr)
        times += 1
    return arr

def part2(array, operations):
    split_candidates = {}
    others = {}
    #{num:quantity}
    zeros = 0

    for num in array:
        if num == 0:
            zeros += 1
        elif len(str(num)) % 2 == 0:
            if num in split_candidates:
                split_candidates[num] += 1
            else:
                split_candidates.update({num: 1})
        else:
            if num in others:
                others[num] += 1
            else:
                others.update({num: 1})
    for i in range(operations):
        zero_num = zeros
        zeros = 0

        new_split_candidates = {}
        new_others = {}
        for num, quantity in split_candidates.items():
            num_str = str(num)
            mid = len(num_str) // 2
            part1 = int(num_str[:mid])
            part2 = int(num_str[mid:])

            for part in [part1, part2]:
                if part == 0:
                    zeros += quantity
                elif len(str(part)) % 2 == 0:
                    if part in new_split_candidates:
                        new_split_candidates[part] += quantity
                    else:
                        new_split_candidates.update({part: quantity})
                else:  # 奇数位数，进入乘以2024
                    if part in new_others:
                        new_others[part] += quantity
                    else:
                        new_others.update({part: quantity})

        for num,quantity in others.items():
            new_num = num * 2024
            if len(str(new_num)) % 2 == 0:
                if new_num in new_split_candidates:
                    new_split_candidates[new_num] += quantity
                else:
                    new_split_candidates.update({new_num: quantity})
            else:
                if new_num in new_others:
                    new_others[new_num] += quantity
                else:
                    new_others.update({new_num: quantity})

        split_candidates = new_split_candidates
        others = new_others
        if 1 in others:
            others[1] += zero_num
        else:
            if zero_num != 0:
                others.update({1: zero_num})

    length = 0
    for value in split_candidates.values():
        length += value
    for value in others.values():
        length += value
    return length + zeros

print(part2(get_input(), 75))
