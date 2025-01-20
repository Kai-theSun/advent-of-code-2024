class Registers:
    def __init__(self, value_A, value_B, value_C):
        self.value_A = value_A
        self.value_B = value_B
        self.value_C = value_C
        self.instruction_pointer = 0

    def getValue(self, name):
        if name == "A":
            return self.value_A
        elif name == "B":
            return self.value_B
        elif name == "C":
            return self.value_C

    def setValue(self, value, name):
        if name == "A":
            self.value_A = value
        elif name == "B":
            self.value_B = value
        elif name == "C":
            self.value_C = value

    def get_operand(self, literal_op):
        if 0 <= literal_op <= 3:
            return literal_op
        elif literal_op == 4:
            return self.getValue("A")
        elif literal_op == 5:
            return self.getValue("B")
        elif literal_op == 6:
            return self.getValue("C")
        elif literal_op == 7:
            return None

    # opcode 0
    def adv(self, lit_operand):
        numerator = self.getValue("A")
        denominator = self.get_operand(lit_operand)
        denominator = 2 ** denominator
        res = numerator // denominator
        self.setValue(res, "A")
        self.instruction_pointer += 2

    # opcode 1
    def bxl(self, lit_operand):
        num1 = self.getValue("B")
        res = num1 ^ lit_operand
        self.setValue(res, "B")
        self.instruction_pointer += 2

    # opcode 2
    def bst(self, lit_operand):
        operand = self.get_operand(lit_operand)
        res = operand % 8
        self.setValue(res, "B")
        self.instruction_pointer += 2

    # opcode 3
    def jnz(self, lit_operand):
        if self.getValue("A") == 0:
            self.instruction_pointer += 2
        else:
            self.instruction_pointer = lit_operand

    # opcode 4
    def bxc(self, lit_operand):
        res = self.getValue("B") ^ self.getValue("C")
        self.setValue(res, "B")
        self.instruction_pointer += 2

    # opcode 5
    def out(self, lit_operand):
        res = self.get_operand(lit_operand) % 8
        self.instruction_pointer += 2
        return res

    # opcode 6
    def bdv(self, lit_operand):
        numerator = self.getValue("A")
        denominator = self.get_operand(lit_operand)
        denominator = 2 ** denominator
        res = numerator // denominator
        self.setValue(res, "B")
        self.instruction_pointer += 2

    # opcode 7
    def cdv(self, lit_operand):
        numerator = self.getValue("A")
        denominator = self.get_operand(lit_operand)
        denominator = 2 ** denominator
        res = numerator // denominator
        self.setValue(res, "C")
        self.instruction_pointer += 2

def part1(initial):
    registers = Registers(initial, 0, 0)
    program = [2,4,1,1,7,5,4,4,1,4,0,3,5,5,3,0]
    pointer = registers.instruction_pointer
    out_put = []
    while pointer + 1 < len(program):
        match program[pointer]:
            case 0:
                registers.adv(program[pointer + 1])
            case 1:
                registers.bxl(program[pointer + 1])
            case 2:
                registers.bst(program[pointer + 1])
            case 3:
                registers.jnz(program[pointer + 1])
            case 4:
                registers.bxc(program[pointer + 1])
            case 5:
                out = registers.out(program[pointer + 1])
                out_put.append(out)
            case 6:
                registers.bdv(program[pointer + 1])
            case 7:
                registers.cdv(program[pointer + 1])
        pointer = registers.instruction_pointer
    return out_put

def part2():
    program = [2, 4, 1, 1, 7, 5, 4, 4, 1, 4, 0, 3, 5, 5, 3, 0]
    initialize = 75750000
    while True:
        registers = Registers(initialize, 0, 0)
        pointer = registers.instruction_pointer
        out_put = []
        while pointer + 1 < len(program):
            match program[pointer]:
                case 0:
                    registers.adv(program[pointer + 1])
                case 1:
                    registers.bxl(program[pointer + 1])
                case 2:
                    registers.bst(program[pointer + 1])
                case 3:
                    registers.jnz(program[pointer + 1])
                case 4:
                    registers.bxc(program[pointer + 1])
                case 5:
                    out = registers.out(program[pointer + 1])
                    out_put.append(out)
                case 6:
                    registers.bdv(program[pointer + 1])
                case 7:
                    registers.cdv(program[pointer + 1])
            pointer = registers.instruction_pointer
            if out_put != program[0:len(out_put)]:
                break
            if len(out_put) > len(program):
                break
        if initialize % 250000 == 0:
            print(initialize)
        if out_put == program:
            return initialize
        else:
            initialize += 1

num = 242
ini_out = part1(num)
print(ini_out)
for i in range(0, 8**5):
    out = part1(i)
    if len(out) == 6 and out[3:] == ini_out:
        print(i)
