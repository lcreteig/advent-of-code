#!/usr/bin/env python3


def check_two_adjacent(number: int):
    num2str = str(number)  # make it iterable
    digit1 = num2str[0]  # start with the first digit
    for digit2 in num2str[1:]:  # loop over all but first digit
        if digit1 == digit2:  # if the next digit is equal
            return True  # stop
        else:
            digit1 = digit2  # shift to the next digit
    return False


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


def n_passwords(start: int, end: int):
    if (len(str(start)) != 6) or (len(str(end)) != 6):
        raise ValueError("The start and/or end of the range is not a 6 digit number")

    n = 0
    for number in range(start, end + 1):
        if check_two_adjacent(number) & check_not_descending(number):
            n += 1
    return n


if __name__ == "__main__":
    print("Part 1: ", n_passwords(124075, 580769))
