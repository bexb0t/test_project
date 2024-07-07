def reverse(x: int) -> int:
    if not in_range(x):
        return 0
    reversed_list = list(str(abs(x)))
    reversed_list.reverse()
    result = int("".join(reversed_list))
    if x < 1:
        result = result * -1
    return result


def in_range(x: int) -> bool:
    min = -2e31
    max = 2e31-1
    return min < x < max

if __name__ == "__main__":
    x = 123
    print(f"x = {x}")
    print(f"result: {reverse(x)}, expected: 321")
    x = -123
    print(f"x = {x}")
    print(f"result: {reverse(x)}, expected: -321")
    x = 120
    print(f"x = {x}")
    print(f"result: {reverse(x)}, expected 21")
    x = -2e32
    print(f"x = {int(x)}")
    print(f"result: {reverse(x)}, expected: 0")
    x = 2e31
    print(f"x = {int(x)}")
    print(f"result: {reverse(x)}, expected: 0")


