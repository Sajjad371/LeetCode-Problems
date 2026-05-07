class Solution(object):
    def findNumbers(self, nums):
        result=0

        for i in nums:
            tem=len(str(i))
            if tem%2==0:
                result+=1
        return result

        
        
       
        