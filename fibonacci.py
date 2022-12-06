def fibonacciVal1(n):  
    """
    This function returns the Fibonacci value.
    It is an uses recursive technique.
    """
    if n == 0:    
        return 0  
    elif n == 1:    
        return 1  
    else:    
        return fibonacciVal1(n-1) + fibonacciVal1(n-2)


def fibonacciVal2(n):  
    """
    This function returns the Fibonacci value.
    It is an implementation of memoization techniques.
    """
    memo = [0] * (n+1)  
    memo[0], memo[1] = 0, 1  
    for i in range(2, n+1):    
        memo[i] = memo[i-1] + memo[i-2]  
    
    return memo[n]


if __name__ == "__main__":
    val1 = fibonacciVal1(6)
    val2 = fibonacciVal2(6)
    print(val1)
    print(val2)