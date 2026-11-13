class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dct = {}
        for n in nums:
            if n not in dct:
                dct[n] = 1
            else:
                dct[n] += 1
        freq = sorted(list(dct), key=dct.get, reverse=True)
        return freq[:k]

            