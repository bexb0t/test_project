from typing import List


def next_permutation(nums: List[int]) -> List[int]:
    list_length = len(nums)
    if list_length <= 1:
        # empty or 1 item list has only one permutation
        return nums
    pivot_index = list_length - 2
    # left to right, compare pairs of numbers looking for left > right
    # iterating through the index num, not the list itself
    while (
        nums[pivot_index] > nums[pivot_index + 1]
    ):  # left = nums[pivot_index],  right = nums[pivot_index+1]
        pivot_index -= 1

    print(f"pivot_index: {pivot_index}, value: {nums[pivot_index]}")

    # if there is a valid pivot
    if pivot_index > 0:
        # find next highest value to the right
        swap_index = list_length - 1
        while nums[swap_index] <= nums[pivot_index]:
            print(f"comparing {nums[swap_index]} to {nums[pivot_index]}")
            swap_index -= 1

        print(f"swap_index: {swap_index}")
        # swap places
        nums[pivot_index], nums[swap_index] = nums[swap_index], nums[pivot_index]

    print(f"nums after swapping: {nums}")
    # we always want to reverse the suffix, just sometimes the suffix is the whole list
    # reverse the items to the right (which will sort them ascending)
    nums[pivot_index + 1 :] = nums[pivot_index + 1 :][::-1]
    return nums


# tests
nums = [1, 2, 3, 6, 5, 4]
result = next_permutation(nums)
expected = [1, 2, 4, 3, 5, 6]
print(f"nums: {nums}, result: {result}, expected: {expected}")
assert result == expected

nums = [9, 8, 7, 6]
result = next_permutation(nums)
expected = [6, 7, 8, 9]
print(f"nums: {nums}, result: {result}, expected: {expected}")
assert result == expected
