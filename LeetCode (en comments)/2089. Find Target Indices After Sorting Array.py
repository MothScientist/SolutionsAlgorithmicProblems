class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        '''
            Let's do the task without sorting.
            We will track the number of elements less than the target and the number of target elements - 
            from here we will get their indices.
        '''
        count_less = 0
        count_target = 0

        for i in nums:
            if i == target:
                count_target += 1
            elif i < target:
                count_less += 1
        
        return [count_less + j for j in range(count_target)]