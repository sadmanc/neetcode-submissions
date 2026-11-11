class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ls, dct, sort = [], {}, {}
        for s in strs:
            change = False
            if "".join(sorted(s)) in sort:
                ls[dct["".join(sorted(s))]].append(s)
                change = True
            if not change:
                sort["".join(sorted(s))] = 0
                ls.append([s])
                dct["".join(sorted(s))] = len(ls) - 1
        return ls    
