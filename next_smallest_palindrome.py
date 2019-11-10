def split_num(num):
    '''
    Splits the number into beg, mid, end numbers.
    Incase of an even length number mid == ''

    Parameters:
        num (int): An integer greater than 9

    Result:
        (beg, mid, end) (str, str, str): The number split into the 3

    Examples:
        1221    -> ('12', '', '21')
        12321   -> ('12', '3', '21')
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

    while True:
        beg, mid, end = split_num(num)
        len_num = len(str(num))

        if num == 10 ** len_num - 1:
            return num + 2
        elif mid == '':
            if not int(beg[::-1]) > int(end):
                beg = str(int(beg) + 1)

            end = beg[::-1]
        else:
            if not int(beg[::-1]) > int(end):
                beg_mid = str(int(beg + mid) + 1)
                beg, mid = beg_mid[:-1], beg_mid[-1]

            end = beg[::-1]

        str_num = beg + mid + end
        num = int(str_num)

        if str_num == str_num[::-1]:
            return num


assert(next_smallest_palindrome(8) == 9)
assert(next_smallest_palindrome(9) == 11)
assert(next_smallest_palindrome(11) == 22)

assert(next_smallest_palindrome(1200) == 1221)
assert(next_smallest_palindrome(12300) == 12321)


assert(next_smallest_palindrome(1221) == 1331)
assert(next_smallest_palindrome(12321) == 12421)

assert(next_smallest_palindrome(1224) == 1331)
assert(next_smallest_palindrome(12324) == 12421)

assert(next_smallest_palindrome(9999) == 10001)
assert(next_smallest_palindrome(99999) == 100001)
