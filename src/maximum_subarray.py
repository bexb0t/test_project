INT_MIN = -103


class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            raise ValueError("Empty array invalid.")
        if len(nums) == 1:
            return sum(nums)
        print(f"Nums: {nums}")
        # first: do we really have to consider every possible value in the array, or can we start with a largest number and consider from there?
        # no= if it's a very very large array that won't work cause the max subarray could just be a huge list of 1's.
        # the thing we DON'T want to do is iterate through every possible subarray becuase we'd be storing every subarray to compare the total.
        # so let's find a way to iterate through the whole subarray just
        # What we really need to know is the max of all possible subarrays with and ending point at the current index
        total_max = INT_MIN  # maxSum #max_so_far
        local_max = 0  # currSum #max_ending_here
        print(f"starting loop. total_max: {total_max}, local_max: {local_max}")
        for i in range(len(nums)):
            # at any point in the list, we just need to know the previous max, and then the current ending here is this cells value, plus the previous max
            prev_local_max = local_max  # delete this
            print(
                f"beginning of loop {i}, prev_local_max: {prev_local_max}, total_max: {total_max}"
            )
            print(f"full array: {nums}")
            print(f"i={i}, subarr:{nums[:i+1]}")
            # our new local max is either current value, or current value + previous local max, depending which is higher
            local_max = max(nums[i], nums[i] + local_max)
            print(
                f"max ending here = max({nums[i]}, {nums[i]} + {prev_local_max}) = {local_max}"
            )
            # our new total max is the max of the existing total max, or our new local max
            total_max = max(total_max, local_max)
            print(f"max so far = max({total_max}, {local_max}) = {total_max}")

        print(f"At the end of the loop, total_max = {total_max}")
        return total_max

        # If the array contains all non-negative numbers, then the problem is trivial; a maximum subarray is the entire array.


# If the array contains all non-positive numbers, then a solution is any subarray of size 1 containing the maximal value of the array (or the empty subarray, if it is permitted).
# Several different sub-arrays may have the same maximum sum.


if __name__ == "__main__":
    solution = Solution()
    nums = [-2, -3, -1, -5]
    expected_output = -1
    print(
        f"nums: {nums}, expected: {expected_output}, result: {solution.maxSubArray(nums)}"
    )


def save_me():

    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    expected_output = 6
    print(
        f"nums: {nums}, expected: {expected_output}, result: {solution.maxSubArray(nums)}"
    )
    nums = [1]
    expected_output = 1
    print(
        f"nums: {nums}, expected: {expected_output}, result: {solution.maxSubArray(nums)}"
    )
    nums = [5, 4, -1, 7, 8]
    expected_output = 23
    print(
        f"nums: {nums}, expected: {expected_output}, result: {solution.maxSubArray(nums)}"
    )
    nums = [-1, -2, -3, -4]
    expected_output = -1
    print(
        f"nums: {nums}, expected: {expected_output}, result: {solution.maxSubArray(nums)}"
    )

    nums = [3, -2, 5, -1, 6, -3, 2, -5, 4]
    expected_output = 11
    print(
        f"nums: {nums}, expected: {expected_output}, result: {solution.maxSubArray(nums)}"
    )

    nums = [1, 2, 3, 4, 5]
    expected_output = 15
    print(
        f"nums: {nums}, expected: {expected_output}, result: {solution.maxSubArray(nums)}"
    )

    nums = [0, -3, 1, 1, -1, 2, -2, 3, -5, 4]
    expected_output = 5
    print(
        f"nums: {nums}, expected: {expected_output}, result: {solution.maxSubArray(nums)}"
    )

    nums = [-5, -4, -3, 2, -1, 2, 1, -5, -4]
    expected_output = 4
    print(
        f"nums: {nums}, expected: {expected_output}, result: {solution.maxSubArray(nums)}"
    )

    nums = [2, -1, 2, 3, 4, -5]
    expected_output = 10
    print(
        f"nums: {nums}, expected: {expected_output}, result: {solution.maxSubArray(nums)}"
    )

    nums = [4, -1, 2, 1]
    expected_output = 6
    print(
        f"nums: {nums}, expected: {expected_output}, result: {solution.maxSubArray(nums)}"
    )

    nums = [-2, -3, 4, -1, -2, 1, 5, -3]
    expected_output = 7
    print(
        f"nums: {nums}, expected: {expected_output}, result: {solution.maxSubArray(nums)}"
    )
