class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        res = [1]*n
        prefix=1
        for i in range(n):
            res[i]=prefix
            prefix*=nums[i]
        postfix=1
        for i in range(n-1,-1,-1):
            res[i]*=postfix
            postfix*=nums[i]
        return res
        # n= len(nums)
        # output = []

        # for i in range(n):
        #     product =1
        #     for j in range(n):
        #         if i!=j:
        #             product *= nums[j]
        #     output.append(product)
        
        # return output
