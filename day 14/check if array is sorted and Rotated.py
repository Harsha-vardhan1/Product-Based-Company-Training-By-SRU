class Solution:
    def check(self, nums: List[int]) -> bool:
        '''s=nums.index(max(nums))
        flag=0
        while(s<len(nums) and nums[s]==max(nums)):
            flag=1
            s+=1
        if(flag==1):
            s-=1
        if(sorted(nums[0:s])==nums[0:s] and sorted(nums[s+1:len(nums)])==nums[s+1:len(nums)]):
            return True
        return False'''
        for i in range(len(nums)):
            nums.insert(0,nums.pop())
            if(nums==sorted(nums)):
                return True
        return False