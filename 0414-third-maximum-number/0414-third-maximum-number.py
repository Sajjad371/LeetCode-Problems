class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num=set(nums)
        n=list(num)
        if(len(n)== 1):
            return n[0]
        if (len(n) == 2):
            if (n[0] >= n[1]):
                return n[0]
            elif n[1] > n[0]:
                return n[1]
        n.remove(max(n))
        n.remove(max(n))
        o=max(n)
        p=int(o)
        return  p      