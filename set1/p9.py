# 9. **Fibonacci Sequence**: Write a Python function that generates the first n numbers in the Fibonacci sequence.
#     - *Input*: 5
#     # - *Output*: "[0, 1, 1, 2, 3]"

def fun(n):
    if n<=1:
        return n
    
    else:
        return fun(n-1)+fun(n-2)


def Fibonacci(n):
     series=[]
     for i in range(n):
        series.append(fun(i))
     return fun
   

print(Fibonacci(5))