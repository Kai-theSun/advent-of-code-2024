index = 0
if_do = True
def get_input():
    memory = ""
    with open("D3_input", "r") as file:
        lines = file.readlines()
        for line in lines:
            memory += line
    return memory

def is_expected(string, expected):
    global index
    if index >= len(string):
        return False
    if string[index] != expected:
        return False
    else:
        index += 1
        return True

def is_digit(string):
    global index
    num_str = ''
    if index >= len(string):
        return None
    while string[index].isdigit():
        num_str += string[index]
        index += 1
        if index >= len(string):
            return None
        # the number can't be the last char which is expected to be ')'
        # so just return when the index has been equal to the length of string
    if num_str == '':
        return None
    else:
        return int(num_str)

def is_valid(string):
    global index, if_do
    res = 0
    if not if_do:
        index += 1
        return False, res
    if not is_expected(string, 'm'):
        index += 1
        return False, res
    # only plus index in the first step, because the afterward invalid char can be 'm'
    # which is the first valid character
    if not is_expected(string, 'u'):
        return False, res
    if not is_expected(string, 'l'):
        return False, res
    if not is_expected(string, '('):
        return False, res
    num1 = is_digit(string)
    if num1 is None:
        return False, res
    if not is_expected(string, ','):
        return False, res
    num2 = is_digit(string)
    if num2 is None:
        return False, res
    if not is_expected(string, ')'):
        return False, res
    res += num1 * num2
    return True, res

def part1(string):
    global index
    summary = 0
    while index < len(string):
        valid, res = is_valid(string)
        if valid:
            summary += res
    return summary

def do_or_dont(string):
    global index, if_do
    if string[index:index+4] == "do()":
        if_do = True
        index += 4
    elif string[index:index+7] == "don't()":
        if_do = False
        index += 7
    else:
        return

def part2(string):
    global index
    summary = 0
    while index < len(string):
        do_or_dont(string)
        valid, res = is_valid(string)
        if valid:
            summary += res
    return summary

print(part1(get_input()))
index = 0
print(part2(get_input()))
