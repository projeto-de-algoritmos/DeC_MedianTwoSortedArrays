class Solution:
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        total_length = len(nums1) + len(nums2)
        if total_length % 2 == 0:
            return (
                findKthElement(nums1, nums2, 0, 0, total_length // 2) +
                findKthElement(nums1, nums2, 0, 0, total_length // 2 + 1)
            ) / 2.0
        else:
            return findKthElement(nums1, nums2, 0, 0, total_length // 2 + 1)


def findKthElement(nums1, nums2, start1, start2, k):
    if start1 >= len(nums1):
        return nums2[start2 + k - 1]
    if start2 >= len(nums2):
        return nums1[start1 + k - 1]
    if k == 1:
        return min(nums1[start1], nums2[start2])

    mid1 = start1 + k // 2 - 1 if start1 + k // 2 - 1 < len(nums1) else len(nums1) - 1
    mid2 = start2 + k // 2 - 1 if start2 + k // 2 - 1 < len(nums2) else len(nums2) - 1

    if nums1[mid1] < nums2[mid2]:
        return findKthElement(nums1, nums2, mid1 + 1, start2, k - (mid1 - start1 + 1))
    else:
        return findKthElement(nums1, nums2, start1, mid2 + 1, k - (mid2 - start2 + 1))