def segregateEvenOdd(l):
    odd_index = -1

    for index in range(0, len(l)):
        if l[index] % 2 == 1:
            if odd_index == -1:
                odd_index = index
        else:
            if index > 0 and odd_index > -1:
                num = l[index]
                l.insert(odd_index, num)
                del l[index + 1]
                odd_index += 1
    return l

if __name__ == '__main__':
    l = [2,1,3,6,4,7,8,5]
    print(segregateEvenOdd(l))
