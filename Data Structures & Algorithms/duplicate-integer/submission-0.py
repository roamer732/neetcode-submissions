class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hash = dict()

        for num in nums:
            if hash.get(num):
                return True
            hash[num] = True
        return False
        
         