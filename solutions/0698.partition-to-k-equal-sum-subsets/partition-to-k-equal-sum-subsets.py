#
# @lc app=leetcode id=698 lang=python3
#
# [698] Partition to K Equal Sum Subsets
#

# @lc code=start


class Solution:
    def canPartitionKSubsets1(self, nums: List[int], k: int) -> bool:
        subsum = [0]*k
        target = sum(nums) / k
        nums.sort(reverse=True)
        n = len(nums)

        def dfs(i):
            if i == n:
                return len(set(subsum)) == 1
            for j in range(k):
                subsum[j] += nums[i]
                if subsum[j] <= target and dfs(i+1):
                    return True
                subsum[j] -= nums[i]
                if not subsum[j]: break
            return False
        return dfs(0)

    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        visited = [0 for i in range(len(nums))]
        target = sum(nums) / k
        def dfs(k, idx, cursum):
            if k == 1 and cursum == target:
                return True
            if cursum == target:
                return dfs(k-1, 0, 0)
            else:
                for i in range(idx, len(nums)):
                    if nums[i] + cursum <= target and not visited[i]:
                        visited[i] = 1
                        if dfs(k, i+1, cursum+nums[i]):
                            return True
                        visited[i] = 0
                return False
        return dfs(k, 0, 0)
                        
# @lc code=end
