class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        nums1=0
        nums2=0
        for i in range(1,n+1):
            if(i%m!=0):
                nums1+=i
            elif(i%m==0):
                nums2+=i
        return nums1-nums2
        
