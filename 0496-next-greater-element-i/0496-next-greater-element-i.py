class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        arr = [-1]*len(nums2)
        out = []
        for i in range(len(nums2)):
            for j in range(i,len(nums2)):
                if nums2[j]>nums2[i]:
                    arr[i] = nums2[j]
                    break
        for i in nums1:
            out.append(arr[nums2.index(i)])
        return out