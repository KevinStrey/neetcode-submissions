from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencias = Counter(nums)
        return [item[0] for item in frequencias.most_common(k)]
        