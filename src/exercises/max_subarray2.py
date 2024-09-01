from typing import List

INT_MIN = -103
LIST_MIN = 1


def max_subarray(nums: List[int]) -> int:
    if len(nums) < LIST_MIN:
        raise ValueError("nums too short")
    # traverse the array once
    current_max = 0
    total_max = INT_MIN
    # store just the computed max of the possible sub arrays before this point
    for i in nums:
        # the max possible subarray is either the previous max + current val,
        # or just current val, whichiever is higher
        current_max = max(current_max + i, i)
        # total max is either current max, or total max, whichever is higher
        total_max = max(current_max, total_max)

    return total_max


nums = [-2, -3, -1, -5]
expected = -1
result = max_subarray(nums)
print(f"nums: {nums}, expected: {expected}, result: {result}")
assert result == expected

nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
expected = 6
result = max_subarray(nums)
print(f"nums: {nums}, expected: {expected}, result: {result}")
assert result == expected


nums = [1]
expected = 1
result = max_subarray(nums)
print(f"nums: {nums}, expected: {expected}, result: {result}")
assert result == expected
