from typing import List


def product_except_self(nums: List[int]) -> List[int]:
    n = len(nums)
    result = [1] * n

    prefix = 1
    # iterate forwards to calculate prefix
    for i in range(n):
        # store the previous calc (or 1 if first time) in the current position
        result[i] = prefix
        # then for the next position, multiply by the current va\lue
        prefix *= nums[i]

    suffix = 1
    # iterate in reverse to calculate suffix
    for i in range(n - 1, -1, -1):
        # multiply whatever is stored in current position (or 1 to start) by the current value
        result[i] *= suffix
        # then for the next position, multiply by current value
        suffix *= nums[i]
    return result


nums = [1, 2, 3, 4]
expected = [24, 12, 8, 6]
result = product_except_self(nums)
print(f"nums: {nums}, expected: {expected}, result: {result}")
assert result == expected

nums = [-1, 1, 0, -3, 3]
expected = [0, 0, 9, 0, 0]
result = product_except_self(nums)
print(f"nums: {nums}, expected: {expected}, result: {result}")
assert result == expected
