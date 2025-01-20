rules_input = []
data_input = []
with open('D5_input1') as file1:
    reader1 = file1.readlines()
    for lines in reader1:
        lines = list(map(int,str(lines).strip().split('|')))
        #print(lines)
        rules_input.append(lines)

with open('D5_input2') as file2:
    reader2 = file2.readlines()
    for lines in reader2:
        lines = list(map(int,str(lines).strip().split(',')))
        data_input.append(lines)
rule = {}
for i in rules_input:
    if i[0] not in rule:
        rule[i[0]] = []
    rule[i[0]].append(i[1])

def need_change(num1, num2):
    if num1 in rule[num2]:
        return True
    else:
        return False

def resort(data):
    correct_count = 0
    incorrect_count = 0
    for nums in data:
        is_correct = True
        for i in range(len(nums)):
            for j in range(0, len(nums) - i - 1):
                if need_change(nums[j], nums[j+1]):
                    nums[j], nums[j+1] = nums[j+1], nums[j]
                    is_correct = False
        index = len(nums) // 2
        if not is_correct:
            incorrect_count += nums[index]
        elif is_correct:
            correct_count += nums[index]
    return correct_count, incorrect_count

print(resort(data_input))