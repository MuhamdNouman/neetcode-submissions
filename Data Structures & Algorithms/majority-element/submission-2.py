class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        map = defaultdict(int)
        res = maxCount = 0

        for n in nums:
            map[n]+=1
            if maxCount < map[n]:
                res = n
                maxCount = map[n]
        return res


        