class Solution(object):
    def runningSum(self, nums):
        sum=0
        n=[]
        for i in nums:
            sum+=i
            n.append(sum)

        return n
            
           
            
        
            
            
       

        
        
        