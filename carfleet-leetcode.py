class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        hashmap = {}
        n = len(position)
        stack = []
        carFleet = n
        for i in range(n):
            hashmap[position[i]] = (target-position[i])/speed[i]
        position.sort()
        for i in position:
            while stack and stack[-1] <= hashmap[i]:
                stack.pop()
                carFleet -= 1
            stack.append(hashmap[i])
        return carFleet
