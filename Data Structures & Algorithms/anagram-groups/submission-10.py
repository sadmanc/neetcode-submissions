class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ls, dct = [], {}
        for s in strs:
            sort_s = "".join(sorted(s))
            if sort_s in dct:
                ls[dct[sort_s]].append(s)
            else:
                ls.append([s])
                dct[sort_s] = len(ls) - 1
        return ls    
