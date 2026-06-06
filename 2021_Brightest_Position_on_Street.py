# You are given a list of street lights. Each light illuminates a segment of the street.
# Each element in lights is [position, range]:
# position = location of the light on the street
# range = distance the light reaches on both sides
# A light at position p with range r illuminates the interval:
# [p−r,p+r]
# The brightness of a position on the street is defined as the number of lights illuminating that position.
# Your task is to return the position with the highest brightness.
# If multiple positions have the same maximum brightness, return the smallest such position.

# Example
# Input: lights = [[-3,2],[1,2],[3,3]]
# Output: -1
# Explanation
# The illuminated ranges are:
# [-5, -1]
# [-1,  3]
# [ 0,  6]
# The point -1 is covered by 2 lights, which is the maximum brightness.

from collections import defaultdict
from typing import List


def brightestPosition(lights: List[List[int]]) -> int:
    events = defaultdict(int)

    # build sweep-line events
    for pos, r in lights:
        start = pos - r
        end = pos + r
        events[start] += 1
        events[end + 1] -= 1

    brightness = 0
    max_brightness = 0
    answer = 0

    # sweep from left to right
    for position in sorted(events):
        brightness += events[position]

        if brightness > max_brightness:
            max_brightness = brightness
            answer = position

    return answer

def main():
    print(brightestPosition([[-3,2],[1,2],[3,3]]))
    print(brightestPosition([[0, 2], [2, 2]]))

if __name__ == "__main__":
    main()