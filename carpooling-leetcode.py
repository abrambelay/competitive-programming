class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        getOn = {}
        getOut = {}
        passangers = 0
        for i in range(len(trips)):
            getOn[trips[i][1]] = getOn.get(trips[i][1],0) + trips[i][0]
            getOut[trips[i][2]] = getOut.get(trips[i][2],0) + trips[i][0]
        for i in range(10001):
            if i in getOut.keys():
                passangers -= getOut[i]
            if i in getOn.keys():
                passangers += getOn[i]
            if passangers>capacity:
                return False
        return True
