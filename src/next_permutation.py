from typing import List, Optional


class Solution:
    def nextPermutation(self, nums: List[int]) -> List[int]:
        # traverse from right to left getting pairs of elements
        for i in reversed(
            range(len(nums))
        ):  # TODO: probably don't need to waste the memory on reversed, can use a while loop
            # find the first pair where the left element is smaller than the right element
            left = nums[i - 1]
            right = nums[i]
            if left < right:
                # left element is the pivot
                pivot_index = i - 1
                # store pivot value since we will change this later
                pivot_value = nums[pivot_index]
                swap_index = self.getSwapIndex(nums, pivot_index)
                # swap the pivot and the next largest element
                if swap_index:
                    # set pivot equal to what we have in swap_index
                    nums[pivot_index] = nums[swap_index]
                    # set swap_index equal to stored pivot value
                    nums[swap_index] = pivot_value
                # TODO: can actually just reverse here
                # arrange the rightmost numbers in the ascending order to get the lowest possible permutation
                nums[(pivot_index + 1) :] = sorted(nums[(pivot_index + 1) :])
                return nums

        # if you get to the beginning and don't find one, just sort the list ascending
        return sorted(nums)

    def getSwapIndex(self, nums: List[int], pivot_index: int) -> Optional[int]:
        """
        find the smallest, rightmost element to the right of the pivot index that is larger than the given value
        """
        # only consider the elements to the right of pivot
        slice = nums[(pivot_index + 1) :]
        swap_val = min(filter(lambda x: x > nums[pivot_index], slice))
        # iterate reversed to get the last/rightmost matching index
        for i in reversed(range(len(nums))):
            if nums[i] == swap_val:
                return i
        return None


if __name__ == "__main__":
    solution = Solution()
    nums = [1, 2, 3]
    print(f"nums: {nums}")
    print(f"result: {solution.nextPermutation(nums)}, expected result: [1,3,2]")

    # TODO: we probably don't need to consider the entire previous set of numbers
    nums = [3, 2, 1]
    print(f"nums: {nums}")
    print(f"result: {solution.nextPermutation(nums)}, expected result: [1,2,3]")

    nums = [1, 1, 5]
    print(f"nums: {nums}")
    print(f"result: {solution.nextPermutation(nums)}, expected result: [1,5,1]")

    nums = [1, 3, 2]
    print(f"nums: {nums}")
    print(f"result: {solution.nextPermutation(nums)}, expected result: [2, 1, 3]")

    nums = [2, 1, 3]
    print(f"nums: {nums}")
    print(f"result: {solution.nextPermutation(nums)}, expected result: [2, 3, 1]")

    nums = [1, 5, 1]
    print(f"nums: {nums}")
    print(f"result: {solution.nextPermutation(nums)}, expected result: [5, 1, 1]")

    nums = [1, 2, 3, 6, 5, 4]
    print(f"nums: {nums}")
    print(
        f"result: {solution.nextPermutation(nums)}, expected result: [1, 2, 4, 3, 5, 6]"
    )

    nums = [1, 2, 3, 6, 2, 4]
    print(f"nums: {nums}")
    print(
        f"result: {solution.nextPermutation(nums)}, expected result: [1, 2, 3, 6, 4, 2]"
    )

    nums = [9, 8, 7, 6]
    print(f"nums: {nums}")
    print(f"result: {solution.nextPermutation(nums)}, expected result: [6, 7, 8, 9]")

    nums = [1, 3, 2, 4, 3]
    print(f"nums: {nums}")
    print(f"result: {solution.nextPermutation(nums)}, expected result: [1, 3, 3, 2, 4]")

    nums = [2, 3, 1, 3, 3]
    print(f"nums: {nums}")
    print(f"result: {solution.nextPermutation(nums)}, expected result: [2, 3, 3, 1, 3]")

    nums = [5, 4, 3, 2, 1]
    print(f"nums: {nums}")
    print(f"result: {solution.nextPermutation(nums)}, expected result: [1, 2, 3, 4, 5]")

    nums = [1, 2, 3, 5, 2, 3]
