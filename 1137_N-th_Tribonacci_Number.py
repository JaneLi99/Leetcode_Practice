def tribonacci(n):
    list = [0, 1, 1]
    for i in range(n - len(list) + 1):
        num_fib = list[i] + list[i + 1] + list[i + 2]
        list.append(num_fib)
    return list[n]

if __name__ == '__main__':
    print(tribonacci(n = 4))
    print(tribonacci(n = 25))