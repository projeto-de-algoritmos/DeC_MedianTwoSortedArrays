# Caso de Teste 1
# Input: nums1 = [1,3], nums2 = [2]
# Output: 2.00000
# Explanation: merged array = [1,2,3] and median is 2.

import medianTwoSortedArrays as ma

nums1 = [1,3]
nums2 = [2]

solution = ma.Solution()
print(f"Sorted arrays: \nnums1: {nums1}\nnums2: {nums2}")
result = solution.findMedianSortedArrays(nums1, nums2)
print(f"Solution: {result}")