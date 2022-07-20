#Leetcode Challenge: combine two arrays and find the median
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        for x in nums2:
            nums1.append(x)
        nums1.sort()
        if len(nums1)%2 == 0:
            x = (len(nums1) / 2) - 1
            y = (len(nums1) / 2)
            z = (float(nums1[int(x)]) + float(nums1[int(y)]))/2
            return z
        else:
            x = ((len(nums1) / 2) + 0.5)
            return nums1[int(x)]
