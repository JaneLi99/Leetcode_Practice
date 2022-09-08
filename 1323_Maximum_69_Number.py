def maximum69Number(num):
    num = str(num)
    if '6' in num:
        num = num.replace('6', '9', 1)
    return int(num)

if __name__ == '__main__':
    print(maximum69Number(num = 9669))
    print(maximum69Number(num = 9699))
    print(maximum69Number(num = 9999))