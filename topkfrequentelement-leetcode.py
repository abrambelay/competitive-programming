class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = collections.Counter(nums).most_common()
        res = []
        for i in range(k):
            res.append(counter[i][0])
        return res
