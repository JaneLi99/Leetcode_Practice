def fib(n):
    list = [0, 1]
    for i in range(n - len(list) + 1):
        num_fib = list[i] + list[i + 1]
        list.append(num_fib)
    return list[n]

if __name__ == '__main__':
    print(fib(n = 2))
    print(fib(n = 3))
    print(fib(n = 4))
    print(fib(n = 5))