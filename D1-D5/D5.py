rules = []
data = []
with open('D5_input1') as file1:
    reader1 = file1.readlines()
    for lines in reader1:
        lines = list(map(int,str(lines).strip().split('|')))
        #print(lines)
        rules.append(lines)

with open('D5_input2') as file2:
    reader2 = file2.readlines()
    for lines in reader2:
        lines = list(map(int,str(lines).strip().split(',')))
        data.append(lines)

rule = {}
for i in rules:
    if i[0] not in rule:
        rule[i[0]] = []
    rule[i[0]].append(i[1])

def move(i,j,lst):
    ele = lst.pop(j)
    lst.insert(i,ele)
    return lst

def search(rule,data):
    count = 0
    for nums in data:
        i = 0
        j=1
        while i < len(nums):
            j = i+1
            while j < len(nums):
                print(type(nums[j]), type(rule[nums[j]]))
                if nums[i] in rule[nums[j]]:
                    nums = move(i,j,nums)
                    j = i
                else:
                    j+=1
            i+=1
    for nums in data:
        index = len(nums) // 2
        count += nums[index]
    return count

print(search(rule,data))
