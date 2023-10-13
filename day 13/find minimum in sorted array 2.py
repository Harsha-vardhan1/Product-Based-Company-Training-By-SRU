class Solution:
    def findMin(self, nums: List[int]) -> int:
       '''i=0
        j=len(nums)-1
        while(i<j):
            mid=(i+j)//2
            if(nums[mid]<nums[mid+1] and nums[mid]<nums[mid-1]):
                return nums[mid]
            elif nums[mid+1]>nums[mid-1]:
                j=mid-1
            else:
                i=mid+1
        return nums[0]'''
       return min(nums)
            