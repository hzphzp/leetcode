#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#
# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
#
# algorithms
# Medium (28.02%)
# Total Accepted:    829.3K
# Total Submissions: 3M
# Testcase Example:  '"abcabcbb"'
#
# Given a string, find the length of the longest substring without repeating
# characters.
# 
# 
# Example 1:
# 
# 
# Input: "abcabcbb"
# Output: 3 
# Explanation: The answer is "abc", with the length of 3. 
# 
# 
# 
# Example 2:
# 
# 
# Input: "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# 
# 
# 
# Example 3:
# 
# 
# Input: "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3. 
# ⁠            Note that the answer must be a substring, "pwke" is a
# subsequence and not a substring.
# 
# 
# 
# 
#
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        indexMap = {}
        start = 0
        maxLen = 0
        for j, c in enumerate(s):
            if c in indexMap and indexMap[c] >= start:
                lenTmp = j - start
                if lenTmp > maxLen:
                    maxLen = lenTmp
                start = indexMap[c] + 1
            indexMap[c] = j
        lenTmp = len(s) - start
        if lenTmp > maxLen:
            maxLen = lenTmp
        return maxLen


if __name__ == "__main__":
    solution = Solution()
    print(solution.lengthOfLongestSubstring('abba'))
    print("a")


