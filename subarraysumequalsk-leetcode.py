class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        hashtable = {0:1}
        prefsum = 0
        for i in range(len(nums)):
            prefsum+=nums[i]
            count+=hashtable.get(prefsum-k,0)
            hashtable[prefsum]=hashtable.get(prefsum,0)+1 
        return count
