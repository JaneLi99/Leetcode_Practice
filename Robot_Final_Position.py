# Problem: Determine the Robot's Final Position
#
# A robot starts at position 0 on a vertical line. It can move one step up or down at a time.
# You are given an integer array moves where:
# 1 represents moving up by one unit.
# -1 represents moving down by one unit.
# After performing all the moves, determine the robot’s final position relative to the starting point.
#
# Return:
# "UP" if the robot ends above the starting position.
# "DOWN" if the robot ends below the starting position.
# "SAME" if the robot ends at the same position as the start.
#
# Example 1
# Input: moves = [1, 1, -1]
# Output: "UP"
# Explanation: Final position = 1, which is above the starting position.
#
# Example 2
# Input: moves = [-1, -1, 1]
# Output: "DOWN"
# Explanation: Final position = -1, which is below the starting position.
#
# Example 3
# Input: moves = [1, -1, 1, -1]
# Output: "SAME"
# Explanation: Final position = 0, which is the same as the starting position.

def finalPosition(moves):
    position = sum(moves)

    if position > 0:
        return "UP"
    elif position < 0:
        return "DOWN"
    else:
        return "SAME"


def main():
    # Test case 1
    moves = [1, 1, -1]
    print("Input:", moves)
    print("Output:", finalPosition(moves))
    print()

    # Test case 2
    moves = [-1, -1, 1]
    print("Input:", moves)
    print("Output:", finalPosition(moves))
    print()

    # Test case 3
    moves = [1, -1, 1, -1]
    print("Input:", moves)
    print("Output:", finalPosition(moves))


if __name__ == "__main__":
    main()