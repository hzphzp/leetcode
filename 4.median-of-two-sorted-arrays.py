#
# @lc app=leetcode id=4 lang=python3
#
# [4] Median of Two Sorted Arrays
#
# https://leetcode.com/problems/median-of-two-sorted-arrays/description/
#
# algorithms
# Hard (25.66%)
# Total Accepted:    393.7K
# Total Submissions: 1.5M
# Testcase Example:  '[1,3]\n[2]'
#
# There are two sorted arrays nums1 and nums2 of size m and n respectively.
# 
# Find the median of the two sorted arrays. The overall run time complexity
# should be O(log (m+n)).
# 
# You may assume nums1 and nums2 cannot be both empty.
# 
# Example 1:
# 
# 
# nums1 = [1, 3]
# nums2 = [2]
# 
# The median is 2.0
# 
# 
# Example 2:
# 
# 
# nums1 = [1, 2]
# nums2 = [3, 4]
# 
# The median is (2 + 3)/2 = 2.5
# 
# 
#
class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        nums1.insert(0, float("-inf"))
        nums1.append(float("inf"))
        nums2.insert(0, float("-inf"))
        nums2.append(float("inf"))
        i = 0
        j = 0
        counts = len(nums1) + len(nums2)
        even = (counts % 2 == 0)
        half = int(counts / 2) if even else int(counts / 2)   # 至少half个在在前面 3个-》1个在前面 4个-》 2个在其那面（大的那个）
        while i < len(nums1) and j < len(nums2) and i + j < half:
            if nums1[i] > nums2[j]:
                pre = nums2[j]
                j += 1
            else:
                pre = nums1[i]
                i += 1
        if even:
            if i >= len(nums1):
                pre = max(nums1[-1], nums2[half - len(nums1) - 1])
                tail = nums2[half - len(nums1)]
                return 0.5 * (pre + tail)
            elif j >= len(nums2):
                pre = max(nums2[-1], nums1[half - len(nums1) - 1])
                tail = nums1[half - len(nums2)]
                return 0.5 * (pre + tail)
            elif i + j >= half:
                return 0.5 * (min(nums1[i], nums2[j]) + pre)
        else:
            if i >= len(nums1):
                tail = nums2[half - len(nums1)]
                return tail
            elif j >= len(nums2):
                tail = nums1[half - len(nums2)]
                return tail
            elif i + j >= half:
                return min(nums1[i], nums2[j])
 



if __name__ == "__main__":
    solution = Solution()
    print(solution.findMedianSortedArrays([1, 2], [3, 4]))
            
            
        

