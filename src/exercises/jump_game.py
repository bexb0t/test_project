# https://leetcode.com/problems/jump-game/description/
from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if 0 in nums:
            #  really the only time you'd get false is if there is a zero and you can't skip past it
            # list.index(search, start, end)
            zero_index = nums.index(0)
            print(f"first zero index: {zero_index}")
            if zero_index == 0:
                # we can never get past the first if the first number is 0
                return False
            return self.canPassZeroIndex(zero_index, nums)
        return True

    def canPassZeroIndex(self, zero_index, nums) -> bool:
        preceding_nums = nums[0:zero_index]
        print(
            f"canPassZero(zero_index={zero_index}, nums={nums}), slice: {preceding_nums}"
        )
        calc_list = [n + index for index, n in enumerate(preceding_nums)]
        highest_reachable_index = max(calc_list)
        print(f"calc_list: {calc_list}")
        print(f"highest reachable index from slice: {highest_reachable_index}")
        if highest_reachable_index > zero_index:
            print("Can get past index.")
            new_start = highest_reachable_index
            remainder_list = nums[new_start:]
            if 0 in remainder_list:
                print(f"Zero found in rest of list- {remainder_list}, recursing.")
                new_index = nums.index(0, new_start, len(nums))
                return self.canPassZeroIndex(new_index, nums)
            else:
                print(
                    f"No more zeros found in remaining list- {remainder_list}, returning true."
                )
                return True
        print("Did not find any path. Returning false.")
        return False


if __name__ == "__main__":
    solution = Solution()
    nums = [5, 0, 0, 3, 0, 0, 1]
    print(f"nums: {nums}")
    print(f"result: {solution.canJump(nums)}, expected result: true")

    # TODO: we probably don't need to consider the entire previous set of numbers
    nums = [4, 0, 0, 3, 0, 0, 1]
    print(f"nums: {nums}")
    print(f"result: {solution.canJump(nums)}, expected result: true")

    nums = [4, 1, 0, 1, 3, 0, 1, 2, 0, 1]
    print(f"nums: {nums}")
    print(f"result: {solution.canJump(nums)}, expected result: true")
