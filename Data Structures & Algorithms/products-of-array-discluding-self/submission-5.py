class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        zero_c = 0
        for num in nums:
            if num:
                prod *= num
            else:
                zero_c += 1
        if zero_c > 1: 
            return [0] * len(nums)

        res = [0] * len(nums)
        
        for i,c in enumerate(nums):
            if zero_c:
                res[i] = 0 if c else prod
            else:
                res[i] = prod // c
        return res
