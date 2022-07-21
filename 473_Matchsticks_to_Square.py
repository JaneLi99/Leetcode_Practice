def makesquare(matchsticks):
   length = sum(matchsticks) // 4
   sides = [0] * 4
   if sum(matchsticks) / 4 != length:
       return False
   matchsticks.sort(reverse = True)

   def backtrack(i):
       if i == len(matchsticks):
           return True

       for j in range(4):
           if sides[j] + matchsticks[i] <= length:
               sides[j] += matchsticks[i]
               if backtrack(i + 1):
                   return True
               sides[j] -= matchsticks[i]
       return False

   return backtrack(0)

if __name__ == '__main__':
    print(makesquare(matchsticks = [1, 1, 2, 2, 2]))
    print(makesquare(matchsticks = [3, 3, 3, 3, 4]))
    print(makesquare(matchsticks = [5,5,5,5,4,4,4,4,3,3,3,3]))