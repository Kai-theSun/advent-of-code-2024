from adodbapi.adodbapi import maxint
from sympy.stats.sampling.sample_numpy import numpy

def get_input():
    with open("D14_input", "r") as file:
        all_robots = []
        lines = file.readlines()
        for line in lines:
            position, velocity = line.strip("\n").split(" ")
            px, py = position[2:].split(",")
            vx, vy = velocity[2:].split(",")
            all_robots.append({"px": int(px), "py": int(py), "vx": int(vx), "vy": int(vy)})
        return all_robots
MAP_WIDE = 101
MAP_TALL = 103

def move(init_info, move_times):
    new_px = (init_info["px"] + init_info["vx"] * move_times) % MAP_WIDE
    new_py = (init_info["py"] + init_info["vy"] * move_times) % MAP_TALL
    return new_px, new_py

def part1(input_data, move_times):
    nums1, nums2, nums3, nums4 = 0, 0, 0, 0
    for item in input_data:
        new_px, new_py = move(item, move_times)
        if new_px < MAP_WIDE//2 and new_py < MAP_TALL//2:
            nums1 += 1
        elif new_px > MAP_WIDE//2 and new_py < MAP_TALL//2:
            nums2 += 1
        elif new_px < MAP_WIDE//2 and new_py > MAP_TALL//2:
            nums3 += 1
        elif new_px > MAP_WIDE//2 and new_py > MAP_TALL//2:
            nums4 += 1
    return nums1 * nums2 * nums3 * nums4

def part2(input_data):
    move_times = 1
    while True:
        unique = True
        new_position = numpy.zeros((MAP_TALL, MAP_WIDE), dtype=int)
        for item in input_data:
            new_px, new_py = move(item, move_times)
            if new_position[new_py][new_px] == 0:
                new_position[new_py][new_px] = 1
            else:
                unique = False
                break
        print(move_times)
        if unique:
            input("unique")
            print_tree(new_position)
            input("continue")
        move_times += 1

def part2func2(input_data):
    min_nums = maxint
    min_idx = 0
    for i in range(10000):
        nums = part1(input_data, i)
        if nums < min_nums:
            min_nums = nums
            min_idx = i
    print(min_nums, min_idx)

# though these 2 functions can both solve the part2 question
# I still think it's a kind of coincidence due to the unique input

def print_tree(new_position):
    for line in new_position:
        str_ = ""
        for i in range(len(line)):
            if line[i] == 0:
                str_ += " "
            else:
                str_ += "*"
        print(str_)

part2(get_input())
