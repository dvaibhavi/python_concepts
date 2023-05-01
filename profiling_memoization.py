# Example of optimizing Python code for performance using memoization and profiling

# Memoization: caching the results of expensive function calls
def fib(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 2:
        return 1
    memo[n] = fib(n-1, memo) + fib(n-2, memo)
    return memo[n]

print(fib(50)) # Output: 12586269025

# Profiling: measuring the performance of a program
import cProfile

def square(x):
    return x**2

def sum_squares(n):
    return sum([square(i) for i in range(n)])

cProfile.run('sum_squares(1000000)')

# Output:
# 1000006 function calls in 0.130 seconds
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
# 1    0.013    0.013    0.130    0.130 <string>:1(<module>)
# 1    0.006    0.006    0.118    0.118 <ipython-input-2-5e6e36948527>:9(sum_squares)
# 1    0.110    0.110    0.110    0.110 {built-in method builtins.sum}
# 1000000    0.002    0.000    0.002    0.000 {built-in method builtins.pow}
