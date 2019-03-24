#
# @lc app=leetcode id=7 lang=python
#
# [7] Reverse Integer
#
# https://leetcode.com/problems/reverse-integer/description/
#
# algorithms
# Easy (25.14%)
# Total Accepted:    617.2K
# Total Submissions: 2.5M
# Testcase Example:  '123'
#
# Given a 32-bit signed integer, reverse digits of an integer.
#
# Example 1:
#
#
# Input: 123
# Output: 321
#
#
# Example 2:
#
#
# Input: -123
# Output: -321
#
#
# Example 3:
#
#
# Input: 120
# Output: 21
#
#
# Note:
# Assume we are dealing with an environment which could only store integers
# within the 32-bit signed integer range: [−2^31,  2^31 − 1]. For the purpose
# of this problem, assume that your function returns 0 when the reversed
# integer overflows.
#
#
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        flag = (x >= 0)
        s = str(abs(x))
        x = [i for i in reversed(s)]
        s = "".join(x)
        x = int(s)
        x = x if flag else 0 - x
        x = x if (x >= - 2^31 and x <= 2^31 -1) else 0
        return x


if __name__ == "__main__":
    solution = Solution()
    print(solution.reverse(1534236469))