def fibonacci(n):
    """
    This function for retruning the nth value of fibonacci series 
    """
    n = int(n)
    if n<1:
        return "please enter a postive number"
    if n == 1:
        return 0
    if n == 2:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)


def lucas(n):
    """
    This function for retruning the nth value of lucas series 
    """
    n = int(n)
    if n<1:
        return "please enter a postive number"
    if n == 1:
        return 2
    if n == 2:
        return 1
    return lucas(n-2) + lucas(n-1)

def sum_series(n,x=0,y=1):
    """
    This function for retruning the nth value of any sumation series. 
    you can determine the first two values for the series to be produced. 
    first arrgument for first value and second one for the second value
    """
    n = int(n)
    if n<1:
        return "please enter a postive number"
    if n == 1:
        return x
    if n == 2:
        return y
    return sum_series(n-1,x,y) + sum_series(n-2,x,y)