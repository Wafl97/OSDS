import time

def fib(n):
    if n < 0:
        print("not valid!")
    elif n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)


if __name__ == "__main__":
    start = time.time()
    print(fib(35))
    end = time.time()
    t = end - start
    print("time",t)

