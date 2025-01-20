def get_input():
    with open("D7_input", "r") as file:
        lines = file.readlines()
        input_result = []
        input_nums = []
        for line in lines:
            result, nums = line.strip("\n").split(": ")
            result = int(result)
            nums = nums.split(" ")
            for i in range(len(nums)):
                nums[i] = int(nums[i])
            input_nums.append(nums)
            input_result.append(result)
        return input_result, input_nums

def check(res, num):
    operator_num = len(num) - 1
    for i in range(2**operator_num):
        operator_oder = []
        for j in range(operator_num):
            temp_bin = (i >> j) & 1
            if temp_bin == 0:
                operator_oder.append("+")
            elif temp_bin == 1:
                operator_oder.append("*")
        result = num[0]
        for k in range(len(operator_oder)):
            if operator_oder[k] == "+":
                result += num[k+1]
            elif operator_oder[k] == "*":
                result *= num[k+1]
        if result == res:
            return True
        else:
            continue
    return False

def check4part2(res, num):
    operator_num = len(num) - 1
    for i in range(3 ** operator_num):
        operator_oder = []
        ternary = ''
        tmp = i
        while tmp > 0:
            ternary = str(tmp % 3) + ternary
            tmp //= 3
        ternary = ternary.zfill(operator_num)
        for j in range(operator_num):
            if ternary[j] == "0":
                operator_oder.append("|")
            elif ternary[j] == "1":
                operator_oder.append("*")
            elif ternary[j] == "2":
                operator_oder.append("+")
        result = num[0]
        for k in range(len(operator_oder)):
            if operator_oder[k] == "+":
                result += num[k+1]
            elif operator_oder[k] == "*":
                result *= num[k+1]
            elif operator_oder[k] == "|":
                temp_str1 = str(result)
                temp_str2 = str(num[k+1])
                result = int(temp_str1 + temp_str2)
            if result >= res:
                break
        if result == res:
            return True
        else:
            continue

def part1(results, numbers):
    res = 0
    for i in range(len(results)):
        result = results[i]
        number = numbers[i]
        if check(result, number):
            res += results[i]
    return res

def part2(results, numbers):
    res = 0
    for i in range(len(results)):
        result = results[i]
        number = numbers[i]
        if check4part2(result, number):
            res += results[i]
        print(f"finish{i}")
    return res

input_result, input_nums = get_input()
print(part2(input_result, input_nums))
