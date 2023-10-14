class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        '''res=0
        i=0
        while(i<len(cost)):
            if(i<len(cost)-1):
             if res+cost[i]<res+cost[i+1]:
                res+=cost[i]
                i+=1
             elif res+cost[i]>=res+cost[i+1]:
                res+=cost[i+1]
                i+=2
            else:
                res+=cost[i]
                i+=1
                break
        return res'''
        a=[0 for i in range(len(cost))]
        a[0]=cost[0]
        a[1]=cost[1]
        for i in range(2,len(cost)):
            a[i]=cost[i]+min(a[i-1],a[i-2])
        return min(a[len(cost)-1],a[len(cost)-2])
            
        