// 509. Fibonacci Number

/* I wrote this solution to the problem a few years ago, 
when my experience in programming was just a couple of days, 
so the solution is bad, but added for the sake of nostalgia :) */

// But seriously, here we need a standard algorithm with caching results

// But the fact that this solution has 100% runtime makes me laugh

class Solution {
public:
    int fib(int n) {
        long long fib = 1, fib1 = 1, b, n0 = 3;
        if (n == 0)
            b = 0;
        if (n == 1)
            b = 1;
        if (n == 2)
            b = 1;
        while (n0 <= n)
        {
            b = fib + fib1;
            fib = fib1;
            fib1 = b;
            n0++;
        }
        return b;
    }
};

