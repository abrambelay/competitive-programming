class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        hashmap = {}
        for i,e in enumerate(s):
            hashmap[e]=i
        size = end = 0
        res = []
        for i,e in enumerate(s):
            size+=1
            end = max(end,hashmap[e])
            if i==end:
                res.append(size)
                size = 0
        return res
