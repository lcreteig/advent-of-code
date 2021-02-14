#!/usr/bin/env python3


def check_adjacent(number: int):
    num2str = str(number)  # make it iterable
    digit1 = num2str[0]  # start with the first digit
    group_sizes = []  # list of all groups of adjacent digits
    grp = 1  # initialize counter for first group
    for digit2 in num2str[1:]:  # loop over all but first digit
        if digit1 == digit2:  # if the next digit is equal
            grp += 1
        else:
            digit1 = digit2  # shift to the next digit
            group_sizes.append(grp)  # we're at the end of this group; remember it
            grp = 1
    group_sizes.append(grp)  # also remember last group
    return group_sizes


def check_not_descending(number: int):
    # make a generator this time instead, for the heck of it
    digits = (int(x) for x in str(number))
    digit1 = next(digits)  # start with the first digit
    for digit2 in digits:
        if digit2 < digit1:
            return False
        else:
            digit1 = digit2
    return True


def n_passwords(start: int, end: int, max_len=None):
    if (len(str(start)) != 6) or (len(str(end)) != 6):
        raise ValueError("The start and/or end of the range is not a 6 digit number")

    n = 0
    # fmt: off
    for number in range(start, end + 1):
        if max_len:  # For Part 2: check if any groups of digits of exactly max_len (2)
            if any(
                [x == max_len for x in check_adjacent(number)]
            ) & check_not_descending(number):
                n += 1
        else:  # For Part 1: check if any groups of digits (at least two consecutive)
            if any(
                [x > 1 for x in check_adjacent(number)]
            ) & check_not_descending(number):
                n += 1
    # fmt: on
    return n


if __name__ == "__main__":
    print("Part 1: ", n_passwords(124075, 580769))
    print("Part 2: ", n_passwords(124075, 580769, max_len=2))
