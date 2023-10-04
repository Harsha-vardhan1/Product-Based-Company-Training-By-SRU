class Solution:
    def thirdMax(self, nums: List[int]) -> int:
       print(sorted(nums))
       l=sorted(list(set((nums))))
       print(l)
       if len(l)<3:
           return max(l)
       else:
            return l[len(l)-3]
