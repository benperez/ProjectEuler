def fib():
    a,b = 1,2
    while 1:
        yield a
        a,b = b,a+b

if __name__ == "__main__":
    a = int(raw_input('Give amount: '))
    f = fib()
    fibs = [f.next() for i in range(a)]
    print sum([j for j in fibs if j % 2 == 0])
