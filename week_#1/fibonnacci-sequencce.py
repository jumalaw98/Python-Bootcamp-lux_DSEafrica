# Python function to display Fibonacci sequence

def recur_fibo(x):
    if x <= 1:
        return x
    else:
        return recur_fibo(x - 1) + recur_fibo(x - 2)

    xterm = 10

    if xterm <= 0:
        print("Person, please enter a positive integer")
    else:
        print("Fibonacci sequence:")
        for i in range(xterm):
            print(recur_fibo(i))


