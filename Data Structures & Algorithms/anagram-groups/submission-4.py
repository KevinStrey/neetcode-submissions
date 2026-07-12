class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = collections.defaultdict(list)
        for i, s in enumerate(strs):
            k = "".join(sorted(s))
            groups[k].append(s)
        
        return list(groups.values())

        