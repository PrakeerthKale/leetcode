
class Solution:
    def findLHS(self, nums: List[int]) -> int:
        dic1={}
        for i in nums:
            if i in dic1:
                dic1[i]+=1
            else:
                dic1[i]=1
        sd= dict(sorted(dic1.items()))
        re=0
        lk=list(sd.keys())
        for i in range(1,len(lk)):
            if(lk[i]-lk[i-1]==1):
                su=sd[lk[i]]+sd[lk[i-1]]
                if(re<su):
                    re=su
        return re