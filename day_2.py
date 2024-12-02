from advent.day_2.main import solve_1

# # Test Input
# with open("./inputs/day_2/test.txt") as f:
#     print(solve_1(f.readlines()))

# #   First Input
# with open("./inputs/day_2/input_1.txt") as f:
#     print(solve_1(f.readlines()))


with open("./inputs/day_2/test.txt") as f:
    print(solve_1(f.readlines(), safety_buffer=1))

# #   First Input
with open("./inputs/day_2/input_1.txt") as f:
    print(solve_1(f.readlines(), safety_buffer=1))
