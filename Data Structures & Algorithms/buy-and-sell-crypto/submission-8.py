class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        p_min = prices[0]
        p_max = prices[0]
        max_diff = 0
        for p in prices:
            if p < p_min:
                print(f'{p} < {p_min}')
                p_min = p
                p_max = p
            if p > p_max:
                print(f'{p} > {p_max}')
                p_max = p
            if (p_max - p_min) > max_diff:
                max_diff = p_max - p_min
                print("atualizou max diff: " + str(max_diff))

        return max_diff
        