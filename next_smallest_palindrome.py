def split_num(num):
    '''
    Splits the number into left, mid, right numbers.
    Incase of an even length number mid == ''

    Parameters:
        num (int): An integer greater than 9

    Result:
        (left, mid, right) (str, str, str): The number split into the 3

    Examples:
        1221    -> ('12', '', '21')
        12340   -> ('12', '3', '40')
    '''
    str_num = str(num)
    str_len = len(str_num)
    str_len_by_2 = str_len // 2

    if str_len % 2 == 0:
        return str_num[:str_len_by_2], '', str_num[str_len_by_2:]
    else:
        return str_num[:str_len_by_2], str_num[str_len_by_2], str_num[str_len_by_2 + 1:]


def next_smallest_palindrome(x):
    '''
    Returns the next smallest palindrome

    Parameters:
        x (int): Whole number

    Returns:
        int: the next smallest palindrome
    '''

    if x < 9:
        return x + 1
    if x < 11:
        return 11

    num = x

    left, mid, right = split_num(num)
    len_num = len(str(num))

    if num == 10 ** len_num - 1:  # Special case. eg: 999 = 10 ^ 3 - 1
        return num + 2
    elif mid == '':
        if not int(left[::-1]) > int(right):  # Rev(Left) Not greather than Right
            left = str(int(left) + 1)

        right = left[::-1]
    else:
        if not int(left[::-1]) > int(right):  # Rev(Left) Not greather than Right
            left_mid = str(int(left + mid) + 1)
            left, mid = left_mid[:-1], left_mid[-1]

        right = left[::-1]

    return int(left + mid + right)


# Basic Test cases
assert(next_smallest_palindrome(8) == 9)
assert(next_smallest_palindrome(9) == 11)
assert(next_smallest_palindrome(11) == 22)
assert(next_smallest_palindrome(15) == 22)

# [Case1 - Odd and Even length numbers] - Rev(Left) > Right
assert(next_smallest_palindrome(1200) == 1221)
assert(next_smallest_palindrome(12300) == 12321)


# Case 2  - Odd and Even length numbers - Rev(Left) <= Right
assert(next_smallest_palindrome(1221) == 1331)
assert(next_smallest_palindrome(12321) == 12421)
assert(next_smallest_palindrome(1224) == 1331)
assert(next_smallest_palindrome(12324) == 12421)

# Special Cases Testcases.
assert(next_smallest_palindrome(9999) == 10001)
assert(next_smallest_palindrome(99999) == 100001)
