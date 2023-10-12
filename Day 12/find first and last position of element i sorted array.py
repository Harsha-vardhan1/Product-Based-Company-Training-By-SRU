class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        i=0
        j=len(nums)-1
        flag=0
        res=[]
        while(i<=j):
            mid=(i+j)//2
            if(nums[mid]==target):
                flag=1
                res.append(mid)
                break
            elif(target<nums[mid]):
                j=mid-1
            else:
                i=mid+1
        if flag==1:
            i=mid
            while(i>=0 and nums[i]==target):
                i-=1
            j=mid+1
            while(j<len(nums) and nums[j]==target):
                j+=1
            return [i+1,j-1]
        else:
            return [-1,-1]


        
