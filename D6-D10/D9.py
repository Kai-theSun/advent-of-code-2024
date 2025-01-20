def get_input():
    with open("D9_input", "r") as file:
        line = file.readline()
        return line
test_data = "2333133121414131402"

def part1(input_data):
    disk_memory = []
    for i in range(0, len(input_data), 2):
        for k in range(int(input_data[i])):
            disk_memory.append(i//2)
        if i+1 >= len(input_data):
            break
        for k in range(int(input_data[i+1])):
            disk_memory.append('.')
    left = 0
    right = len(disk_memory) - 1
    while left < right:
        if disk_memory[left] != '.':
            left += 1
            continue
        if disk_memory[right] == '.':
            right -= 1
            continue
        disk_memory[left], disk_memory[right] = disk_memory[right], disk_memory[left]
        left += 1
        right -= 1
    check_sum = 0
    for i in range(len(disk_memory)):
        if disk_memory[i] == '.':
            break
        else:
            check_sum += disk_memory[i] * i
    return check_sum

def try_condense(file_block, blank_block, right):
    block_length = file_block[right]["length"]
    for i in range(len(blank_block)):
        if blank_block[i]["length"] <= 0:
            continue
        if blank_block[i]["start_idx"] >= file_block[right]["start_idx"]:
            return
        if blank_block[i]["length"] >= block_length:
            blank_block[i]["length"] -= block_length
            file_block[right]["start_idx"] = blank_block[i]["start_idx"]
            blank_block[i]["start_idx"] += block_length
            return

def part2(input_data):
    blank_block = []
    #{start_idx:idx, length:l}
    file_block = []
    #{file_id:id, start_idx:idx, length:l}
    idx = 0
    for i in range(0, len(input_data), 2):
        file_block.append({"file_id":i//2, "start_idx":idx, "length":int(input_data[i])})
        idx += int(input_data[i])
        if i+1 >= len(input_data):
            break
        blank_block.append({"start_idx":idx, "length":int(input_data[i+1])})
        idx += int(input_data[i+1])

    for i in range(len(file_block) - 1, 0, -1):
        try_condense(file_block, blank_block, i)

    check_sum = 0
    for i in range(len(file_block)):
        start_idx = file_block[i]["start_idx"]
        for j in range(file_block[i]["length"]):
            check_sum += (start_idx + j) * file_block[i]["file_id"]
    return check_sum

print(part1(get_input()))
print(part2(get_input()))