class Solution:
    def isGood(self, nums: List[int]) -> bool:
      nums.sort()
      m=max(nums)
      l=len(nums)
      if(nums[l-1]==m and nums.count(m)==2 and l-1==m):
          flag=1
          for i in range(l-2):
              if(nums.count(i)>1):
                  flag=0
                  break
          if(flag==1):
              return True
      return False


