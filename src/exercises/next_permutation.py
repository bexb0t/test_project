from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> List[int]:
        list_length = len(nums)
        print(f"Nums given: {nums}, length: {list_length}")
        if list_length <= 1:
            return nums

        # Step 1: Find the first number that is smaller than the number to its right
        # NOTE: This is the first occasion where the numbers to the right of the index are not in descending order
        pivot_idx = list_length - 2  # starting from 2 from the end
        while (
            pivot_idx >= 0 and nums[pivot_idx] >= nums[pivot_idx + 1]
        ):  # nums[idx] =left, nums[idx +1 ] = right
            pivot_idx -= 1
        print(f"Pivot index: {pivot_idx}, value: {nums[pivot_idx]}")

        if pivot_idx >= 0:  # If there is a valid pivot
            # Step 2: Find next largest number from the pivot
            swap_index = list_length - 1
            # Since we know all numbers to the right of pivot are in descending order, we can just grab the rightmost number that is larger
            while (
                nums[swap_index] <= nums[pivot_idx]
            ):  # starting from the last item, iterate unti you find one larger than pivot
                swap_index -= 1

            # Step 3: Swap the pivot with this identified element
            print(
                f"Next highest number identified. Index: {swap_index}, val: {nums[swap_index]}"
            )
            nums[pivot_idx], nums[swap_index] = nums[swap_index], nums[pivot_idx]
            print(f"Swapped these values, nums is now: {nums}")

        # Step 4: Reverse the suffix
        nums[pivot_idx + 1 :] = nums[pivot_idx + 1 :][::-1]
        print(
            f"Reversed all items to the right of pivot index {pivot_idx}, final value is: {nums}"
        )
        return nums


if __name__ == "__main__":
    solution = Solution()

    nums = [9, 8, 7, 6]
    print(f"nums: {nums}")
    print(f"result: {solution.nextPermutation(nums)}, expected result: [6, 7, 8, 9]")
