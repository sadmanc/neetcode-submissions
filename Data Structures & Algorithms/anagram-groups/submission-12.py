class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dct = {}
        for s in strs:
            sort_s = "".join(sorted(s))
            if sort_s in dct:
                dct[sort_s].append(s)
            else:
                dct[sort_s] = [s]
        return list(dct.values())