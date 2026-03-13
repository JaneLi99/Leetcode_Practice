# Canonical - Technical Exercise - Python OA 1
# There are two ISBN standards: ISBN-10 and ISBN-13.

# ISBN-10 is made up of 9 digits followed by a (right-most) check digit (which may be 'X') and
# ISBN-13 is made up of 12 digits plus the check digit. Spaces and hyphens may be included in a code, but are not significant.
# This means that 9780471486480 is equivalent to 978-0-471-48648-0 and 978 0 471 48648 0.
#
# The check digit for ISBN-10 is calculated by multiplying each digit (excluding the check digit)
# by its position (i.e., 1 x 1st digit, 2 x 2nd digit, etc.), summing these products together and
# taking modulo 11 of the result (with 'X' being used if the result is 10).
#
# The check digit for ISBN-13 is calculated by multiplying each digit (excluding the check digit) alternately
# by 1 or 3 (i.e., 1 x 1st digit, 3 x 2nd digit, 1 x 3rd digit, 3 x 4th digit, etc.), summing these products together,
# taking modulo 10 of the result, subtracting this value from 10,
# and then taking modulo 10 of the result again to produce a single digit.

# Create a function that takes a string and returns true if it is a valid ISBN13 or a valid ISBN10 and false otherwise.
# The signature of your function should be:
# You may implement other functions called by your function if you wish.
# The output should be a boolean.
#
# Sample Input & Output
# TEST_CASES = [
#     ("9780471486480", True),
#     ("978-1-56619-909-2", False),
#     ("978-1-56619-909-4", True),
#     ("0471958695", False),
#     ("0-8044-2957-X", True)
# ]

def solve(incoming: str) -> bool:
    incoming = incoming.replace("-", "").replace(" ", "")

    if len(incoming) == 10:
        is_valid = True
        for i in range(len(incoming) - 1):
            if not (incoming[i].isdigit() or incoming[i] == "X"):
                is_valid = False
                break

        if not (incoming[-1].isdigit() or incoming[-1] == "X"):
            is_valid = False

        if is_valid:
            sum_check = 0
            for i in range(len(incoming) - 1):
                sum_check += (i + 1) * int(incoming[i])
            digit_check = incoming[9]
            if digit_check == "X":
                sum_check += 10 * 10
            else:
                sum_check += 10 * int(digit_check)

        return sum_check % 11 == 0

    elif len(incoming) == 13 and incoming.isdigit():
        sum_check = 0
        for i in range(len(incoming) - 1):
            if i % 2 == 0:
                sum_check += int(incoming[i])
            else:
                sum_check += 3 * int(incoming[i])

        digit_check = int(incoming[-1])
        calculate_check = (10 - (sum_check % 10)) % 10
        return calculate_check == digit_check

    return False

if __name__ == "__main__":
    solve("9780471486480")