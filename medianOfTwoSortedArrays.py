# Simple Inital Solution

import math
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums = nums1 + nums2
        nums.sort()
        length = len(nums)
        remainder = length % 2
        if remainder == 0:
            mp = length/2
            value1 = float(nums[mp-1])
            value2 = float(nums[mp])
            ans = (value1+value2)/2
            print(ans)
        else:
            mp = math.ceil(length/2)
            ans = nums[int(mp)]
        return ans

        
