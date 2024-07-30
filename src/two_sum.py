from typing import Dict, List
from unittest import TestCase

# Given an array of integers nums and an integer target, return indices
# of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution,
# and you may not use the same element twice.


def two_sums(nums: List[int], target: int) -> List[int]:
    pair: List[int] = []
    seen: Dict[int, int] = {}

    # iterate through array once
    for i in range(len(nums)):
        # find the diff between current element and target
        complement = target - nums[i]

        # see if this number exists in the pairs table
        # if so, then we found the pair
        if complement in seen:
            # returning the *index* not the value
            pair = [seen[complement], i]

        # add current number to hash table for use later
        # key: number, value: index
        seen[nums[i]] = i

    return pair


testcase = TestCase()

nums = [2, 7, 11, 15]
target = 9
expected = [0, 1]
# Because nums[0] + nums[1] == 9, we return [0, 1].
result = two_sums(nums, target)
print(f"nums: {nums}, target: {target}, expected: {expected}, result: {result}")
testcase = TestCase()
testcase.assertCountEqual(expected, result)

nums = [3, 2, 4]
target = 6
expected = [1, 2]
result = two_sums(nums, target)
print(f"nums: {nums}, target: {target}, expected: {expected}, result: {result}")
testcase = TestCase()
testcase.assertCountEqual(expected, result)


nums = [3, 3]
target = 6
expected = [0, 1]
result = two_sums(nums, target)
print(f"nums: {nums}, target: {target}, expected: {expected}, result: {result}")
testcase = TestCase()
testcase.assertCountEqual(expected, result)
