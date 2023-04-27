# Name: Joshua Jansen
# OSU Email: Jansejos@oregonstate.edu
# Course: CS325
# Assignment: 4

def max_independent_set(nums):
    """
    Finds a subsequence of non-consecutive numbers that would be the max sum.
    :param nums: An array of integers
    :return: A subarray of integers that are the maximum sum of non-consecutive numbers of the given array
    """
    n = len(nums)
    dp = [0] * (n + 1)
    dp[1] = nums[0]
    sum_nums = []

    for i in range(2, (n + 1)):
        dp[i] = max(dp[i - 1], dp[i - 2] + nums[i - 1], nums[i - 1])

    while n > 0:
        if dp[n] >= 0:
            if dp[n] == dp[n - 1]:
                n -= 1
            else:
                sum_nums.append(nums[n - 1])
                n -= 2
        else:
            n -= 1

    return sum_nums[::-1]