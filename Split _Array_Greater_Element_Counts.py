# Problem: Split an Array Based on Greater Element Counts
# You are given an integer array A. Your task is to split it into two arrays B and C using the following rules.
# Process each element a in A from left to right:
# Let countB be the number of elements in B that are greater than a.
# Let countC be the number of elements in C that are greater than a.
# If countB > countC, append a to array B.
# If countB < countC, append a to array C.
# If countB == countC, append a to the array with fewer elements.
# If both arrays have the same length, append a to B.
# Return the two arrays B and C.

def splitArray(A):
    B = []
    C = []

    for a in A:
        countB = sum(1 for x in B if x > a)
        countC = sum(1 for x in C if x > a)

        if countB > countC:
            B.append(a)
        elif countC > countB:
            C.append(a)
        else:
            if len(B) <= len(C):
                B.append(a)
            else:
                C.append(a)
    return B, C


def main():
    # Test case 1
    A = [5, 3, 8, 2]
    B, C = splitArray(A)
    print("Input:", A)
    print("B:", B)
    print("C:", C)
    print()

    # Test case 2
    A = [4, 1, 6, 2, 7]
    B, C = splitArray(A)
    print("Input:", A)
    print("B:", B)
    print("C:", C)
    print()

    # Test case 3
    A = [10, 5, 3, 8, 6]
    B, C = splitArray(A)
    print("Input:", A)
    print("B:", B)
    print("C:", C)


if __name__ == "__main__":
    main()