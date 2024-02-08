class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        # n - number of cubes
        # k - number of faces

        @cache
        def func(_n, _target):
            if _target < _n or _target > _n * k:  # when it is impossible to get the 'target' in the current situation
                return 0
            if _n == 1 or _target == _n * k:  # when there is only one option for obtaining 'target'
                return 1
            s = 0
            for i in range(1, k + 1):  # for each face of the cube
                s += func(_n - 1, _target - i)
                # target - i: since each cube can give a result from 1 to k, we subtract this result in the loop after subtracting each cube
            return s % (10**9 + 7)
            
        return func(n, target)