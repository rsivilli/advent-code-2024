import re

mul_command_pattern = r"mul\((?P<arg1>\d+),(?P<arg2>\d+)\)"
cond_command_pattern = r"do\(\)+|don't\(\)|mul\(\d+,\d+\)"
ignore_command_pattern = r"don't\(\)(mul\(\d+,\d+\))*"


def solve_1(str_input: str) -> int:
    """extracts and sums all commands"""
    out = 0
    for m in re.finditer(mul_command_pattern, str_input):
        out += int(m.group("arg1")) * int(m.group("arg2"))
    return out


def solve_2(str_input: str) -> int:
    """filters out ignored commands and sums all valid commands"""
    matches = re.findall(cond_command_pattern, str_input)  # removes all stuff we don't care about to simplify next step
    clean_input = re.sub(ignore_command_pattern, "", "".join(matches))  # removes all ignored commands
    return solve_1(clean_input)  # processes it with the logic above
