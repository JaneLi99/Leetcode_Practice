"""
Write a function that given a string S of letter "L" and "R", denoting the types of shoes in line (left and right),
returns the maximum number of intervals such that each interval contains an equal number of left and right shoes.
For example, given S = "RLRRLLRLRRLL", the function shoulf return 4, because S can be split into intervals: "RL",
"RRLL", "RL" and "RRLL". Note that the intervals do not have to be of the same size.
Given S = "RLLLRRRLLR", the function should return 4, because S can be split into intervals: "RL", "LLRR", "RL"
and "LR".
Given S = "LLRLRLRLRLRLRR", the function should return 1.
"""
def solution(S):
   R_count = L_count =  0
   total_count = 0

   for letter in S:
       if(letter == 'R'):
           R_count += 1
       elif (letter == 'L'):
           L_count += 1

       if (R_count == L_count):
           total_count += 1
           R_count = 0
           L_count = 0

   return total_count

if __name__ == '__main__':
    print(solution(S = "RLRRLLRLRRLL"))
    # Output = 4
    print(solution(S = "RLLLRRRLLR"))
    # Output = 4
    print(solution(S = "LLRLRLRLRLRLRR"))
    # Output = 1