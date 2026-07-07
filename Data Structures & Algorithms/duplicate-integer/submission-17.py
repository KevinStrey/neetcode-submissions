class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        size_list = len(nums)
        size_set = len(set(nums))
        print(size_list)
        print(size_set)
        if size_list == size_set:
            return False
        else:
            return True

