def is_report_safe(
    line: str, max_change: int = 3, min_change: int = 1, safety_buffer: int = 0, vals: list[int] | None = None
) -> bool:
    vals = vals or [int(val) for val in line.split()]  # split lines into individual numbers
    sign = None
    error_count = 0
    for i in range(len(vals) - 1):
        diff = vals[i + 1] - vals[i]
        if abs(diff) > max_change or abs(diff) < min_change:
            error_count += 1
        # If this is the first diff, check the slope (it is either greater that zero for a positive slop or less than zero for a negative slope)
        elif sign is None:
            sign = diff > 0
        # If the slope ever changes from the original slope, it is not safe
        elif sign != (diff > 0):
            error_count += 1
        if error_count > 0:
            if error_count > safety_buffer:
                return False
            else:
                for i in range(len(vals)):
                    tmp = vals.copy()
                    tmp.pop(i)
                    if is_report_safe(line, max_change, min_change, safety_buffer - 1, vals=tmp):
                        return True
                return False

    return True


def solve_1(lines: list[str], max_change: int = 3, min_change: int = 1, safety_buffer: int = 0) -> int:
    safe_count = 0
    for line in lines:
        line = line.strip()
        if is_report_safe(line, max_change, min_change, safety_buffer):
            safe_count += 1

    return safe_count
