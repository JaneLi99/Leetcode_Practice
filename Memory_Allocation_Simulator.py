# You are given an integer array memory representing a block of memory:
# 0 indicates the memory cell is free
# 1 indicates the memory cell is occupied
# You need to support two types of operations:
# Allocate memory
# Free allocated memory
# Allocation Rules
# When allocating memory of size k:
# The starting index of the allocated block must be a multiple of 8.
# There must be at least k consecutive free cells (0) starting from that index.
# If allocation is successful, those cells become occupied (1).
# Freeing Rules
# When freeing memory starting at index start with size k:
# You must verify that the memory block [start, start + k - 1] was previously allocated by the user.
# If valid, those cells become free (0) again.
# Return Value
# Allocation returns the starting index of the allocated block, or -1 if allocation fails.
# Freeing returns true if successful, otherwise false.
#
# Example
# Input:
# memory = [0,0,0,0,0,0,0,0,0,0,0,0]
# allocate(4)
# Output:0
# Explanation: Index 0 is a multiple of 8 and has enough free space.
#
# Example 2
# Input:
# memory = [1,1,1,1,1,1,1,1,0,0,0,0]
# allocate(4)
# Output:8
# Explanation: The next valid starting position that is a multiple of 8 is index 8.

def allocate(memory, size):
    n = len(memory)
    for i in range(0, n, 8):  # start must be multiple of 8
        if i + size <= n and all(memory[j] == 0 for j in range(i, i + size)):
            for j in range(i, i + size):
                memory[j] = 1
            return i
    return -1


def free(memory, start, size):
    n = len(memory)

    if start + size > n:
        return False

    for j in range(start, start + size):
        if memory[j] != 1:
            return False

    for j in range(start, start + size):
        memory[j] = 0

    return True


def main():
    memory = [0] * 16

    print("Initial memory:", memory)

    pos = allocate(memory, 4)
    print("allocate(4) →", pos)
    print(memory)

    pos = allocate(memory, 6)
    print("allocate(6) →", pos)
    print(memory)

    success = free(memory, 0, 4)
    print("free(0,4) →", success)
    print(memory)

    pos = allocate(memory, 8)
    print("allocate(8) →", pos)
    print(memory)


if __name__ == "__main__":
    main()