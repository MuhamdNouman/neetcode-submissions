class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        element = nums[0]
        count = 0
        for e in nums:
            if e == element:
                count += 1
            else:
                count -= 1
                if count < 0:
                    count = 1
                    element = e
        return element
        
        
        