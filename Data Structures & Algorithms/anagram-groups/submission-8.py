class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ls, dct, sort = [], {}, {}
        for s in strs:
            sort_s = "".join(sorted(s))
            change = False
            if sort_s in sort:
                ls[dct["".join(sorted(s))]].append(s)
                change = True
            if not change:
                sort[sort_s] = 0
                ls.append([s])
                dct[sort_s] = len(ls) - 1
        return ls    
