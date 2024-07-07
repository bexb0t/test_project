# leetcode format
class Solution:
    def reverse(self, x: int) -> int:
        if not self.in_range(x):
            return 0
        reversed_list = list(str(abs(x)))
        reversed_list.reverse()
        result = int("".join(reversed_list))
        if x < 1:
            result = result * -1
        return result

    def in_range(self, x: int) -> bool:
        min = -2e31
        max = 2e31 - 1
        return min < x < max


if __name__ == "__main__":
    solution = Solution()
    x = 123
    print(f"x = {x}")
    print(f"result: {solution.reverse(x)}, expected: 321")
    x = -123
    print(f"x = {x}")
    print(f"result: {solution.reverse(x)}, expected: -321")
    x = 120
    print(f"x = {x}")
    print(f"result: {solution.reverse(x)}, expected 21")
    x = int(-2e32)
    print(f"x = {int(x)}")
    print(f"result: {solution.reverse(x)}, expected: 0")
    x = int(2e31)
    print(f"x = {int(x)}")
    print(f"result: {solution.reverse(x)}, expected: 0")
