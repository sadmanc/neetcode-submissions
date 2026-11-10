class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        no_dupes = set()
        for i in nums:
            no_dupes.add(i)
        return len(no_dupes) < len(nums)