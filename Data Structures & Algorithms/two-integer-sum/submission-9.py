class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map_valor_indice = {}
        
        for i,n in enumerate(nums):
            diff = target - n

            if diff in map_valor_indice:
                return [map_valor_indice[diff], i]

            map_valor_indice[n] = i