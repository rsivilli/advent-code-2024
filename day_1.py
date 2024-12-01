from advent.day_1.main import solve_1, solve_2

with open("./inputs/day_1/input.txt") as f:
    input_list = f.readlines()
    print(solve_1(input_str=input_list))
    print(solve_2(input_str=input_list))
