def get_input():
    with open("D13_input", "r") as file:
        total_input = []
        lines = file.readlines()
        item = {}
        for line in lines:
            line = line.strip("\n")
            if line:
                title, value = line.split(":")
            else:
                item = {}
                continue
            if title == "Button A":
                tempx, tempy = value.strip().split(",")
                x = int(tempx[2:])
                y = int(tempy[2:])
                item.update({"Ax":x, "Ay":y})
            elif title == "Button B":
                tempx, tempy = value.strip().split(",")
                x = int(tempx[2:])
                y = int(tempy[2:])
                item.update({"Bx": x, "By": y})
            elif title == "Prize":
                tempx, tempy = value.strip().split(",")
                x = int(tempx[2:])
                y = int(tempy[3:])
                item.update({"Total_x":x, "Total_y":y})
                total_input.append(item)
            else:
                continue
        return total_input

def calculate(Ax, Ay, Bx, By, Tx, Ty):
    max_times = 100
    for m in range(max_times+1):
        for n in range(max_times+1):
            if Ax * m + Bx * n == Tx and Ay * m + By * n == Ty:
                return 3 * m + n
    return 0

def calculate4part2(Ax, Ay, Bx, By, Tx, Ty):
    z = Ax*By-Ay*Bx
    if (Ty*Ax-Tx*Ay)%z == 0:
        n = (Ty*Ax-Tx*Ay)//z
        if (Tx*By-Ty*Bx)%z == 0:
            m = (Tx*By-Ty*Bx)//z
            return 3 * m + n
    return 0

def part1(input_data):
    res = 0
    for item in input_data:
        res += calculate(item["Ax"], item["Ay"], item["Bx"], item["By"], item["Total_x"], item["Total_y"])
    return res

def part2(input_data):
    res = 0
    for item in input_data:
        res += calculate4part2(item["Ax"], item["Ay"], item["Bx"], item["By"], item["Total_x"]+10000000000000, item["Total_y"]+10000000000000)
    return res

print(part2(get_input()))
