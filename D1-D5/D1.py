def get_input():
    with open("D1_input", "r") as file:
        lines = file.readlines()
        arr1, arr2 = [], []
        for line in lines:
            x1, x2 = line.split("   ")
            x1 = int(x1)
            x2 = int(x2)
            arr1.append(x1)
            arr2.append(x2)
        return arr1, arr2

def part1(arr1, arr2):
    sum = 0
    arr1.sort()
    arr2.sort()
    for i in range(len(arr1)):
        sum += abs(arr1[i] - arr2[i])
    return sum

def part2(arr1, arr2):
    sum = 0
    for i in range(len(arr1)):
        sum += arr1[i] * arr2.count(arr1[i])
    return sum

arr1, arr2 = get_input()
print(part1(arr1, arr2))
print(part2(arr1, arr2))
