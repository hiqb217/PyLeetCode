class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        numEven = 0
        for num in nums:
            numDig = 0
            while num >= 1:
                num = num / 10.0
                numDig += 1
            if numDig % 2 == 0:
                numEven += 1
        return numEven
