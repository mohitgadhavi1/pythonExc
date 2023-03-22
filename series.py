def fibonacci(n):
    """Returns the first n numbers in the Fibonacci series."""
    if n <= 0 :
        return []
    elif n == 1 :
        return [0]
    else :
        fib_series = [0,1]
        for i in range(2,n):
            fib_series.append(fib_series[i-1] + fib_series[i-2])
        return fib_series
    
def exponential(base,n):
    """Returns the first n numbers in the exponential series with the given base."""
    exp_series = []
    for i in range(n):
        exp_series.append(base ** i)
    return exp_series
