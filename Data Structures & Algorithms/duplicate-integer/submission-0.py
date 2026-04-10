class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        Duplicates = []
        for number in nums:
            if number in Duplicates:
                return True
            else:
                Duplicates.append(number)

        return False