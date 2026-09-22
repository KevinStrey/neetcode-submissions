class Solution:
    def search(self, nums: List[int], target: int) -> int:
        inf = 0
        sup = len(nums)-1
        while(inf <= sup):
            m = (inf + sup) // 2
            if(nums[m] == target):
                return m
            if target < nums[m]:
                sup = m - 1
            else:
                inf = m + 1
        return -1