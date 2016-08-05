#!/usr/bin/env python
# HW04_ch08_ex04

# The following functions are all intended to check whether a string contains
# any lowercase letters, but at least some of them are wrong. For each
# function, describe (is the docstring) what the function actually does.
# You can assume that the parameter is a string.

# Do not merely paste the output as a counterexample into the documentation
# string, explain what is wrong.

###############################################################################
# Body


def any_lowercase1(s):
    """ Checks only the first character for lower case
    """
    for c in s:
        if c.islower():
            return True
        else:
            return False


def any_lowercase2(s):
    """Checks static stirng 'c' if lower. Always returns True
    """
    for c in s:
        if 'c'.islower():
            return 'True'
        else:
            return 'False'


def any_lowercase3(s):
    """Checks all chars, but only the last char check for lower case is returned.
    """
    for c in s:
        flag = c.islower()
    return flag


def any_lowercase4(s):
    """Works as expected. CORRECT!
    """
    flag = False
    for c in s:
        flag = flag or c.islower()
    return flag


def any_lowercase5(s):
    """If even a single upper case letter is present, it returns false.
    """
    for c in s:
        if not c.islower():
            return False
    return True


###############################################################################
def main():

    print(any_lowercase5("thisstringmessesupthefunction"))
    print(any_lowercase5("THs"))

if __name__ == '__main__':
    main()
