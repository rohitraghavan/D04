#!/usr/bin/python2.4 -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

# Additional basic string exercises


# D. verbing
# Given a string, if its length is at least 3,
# add 'ing' to its end.
# Unless it already ends in 'ing', in which case
# add 'ly' instead.
# If the string length is less than 3, leave it unchanged.
# Return the resulting string.
import re

def verbing(s):
    # +++your code here+++
    #if length is more than or equal to 3
    if len(s) >= 3:
        if (s[-3:] == 'ing'): # is the suffix is ing - return string with ly
            return s+'ly'
        else: # else add ing to the string
            return s+'ing'
    else: # if length is less than 3 return the same string
        return s


# E. not_bad
# Given a string, find the first appearance of the
# substring 'not' and 'bad'. If the 'bad' follows
# the 'not', replace the whole 'not'...'bad' substring
# with 'good'.
# Return the resulting string.
# So 'This dinner is not that bad!' yields:
# This dinner is good!
def not_bad(s):
    # +++your code here+++
    patterns = ['not','bad']
    val = s
    val1 = s.find(patterns[0]) # find the position of patterns in the string
    val2 = s.find(patterns[1])
    if val2 > val1: # check if bad occurs after not
        return re.sub('not (.*?) bad','good',s) # if yes, substitute everything after not
        #upto bad with good
    else: # of there is not bad after not, return the string
        return s

# F. front_back
# Consider dividing a string into two halves.
# If the length is even, the front and back halves are the same length.
# If the length is odd, we'll say that the extra char goes in the front half.
# e.g. 'abcde', the front half is 'abc', the back half 'de'.
# Given 2 strings, a and b, return a string of the form
#  a-front + b-front + a-back + b-back
def front_back(a, b):
    # +++your code here+++
    #find half the length of the string
    half_a = len(a)/2
    half_b = len(b)/2
    string_val = ''#initiate a new string
    if half_a  == int(half_a):# check if half of length is integer (even) or float (odd)
        if half_b == int(half_b):# check if half of length is integer (even) or float (odd)
             #if it is integer, split the strings and add them
            string_val = a[:int(half_a)] + b[:int(half_b)] + a[int(half_a):] + b[int(half_b):]
        else: # if b is odd, add the extra word to the first part
             string_val = a[:int(half_a)] + b[:int(half_b)+1] + a[int(half_a):] + b[int(half_b)+1:]
    elif half_b == int(half_b): # if only b is even, add the extra letter to first part of a
        string_val = a[:int(half_a)+1] + b[:int(half_b)] + a[int(half_a)+1:] + b[int(half_b):]
    else:#if both are odd, add the extra letter to first part of a and b
        string_val = a[:int(half_a)+1] + b[:int(half_b)+1] + a[int(half_a)+1:] + b[int(half_b)+1:]
    return string_val


# Simple provided test() function used in main() to print
# what each function returns vs. what it's supposed to return.
def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{} got: {} expected: {}'.format(prefix, repr(got), repr(expected)))


# main() calls the above functions with interesting inputs,
# using the above test() to check if the result is correct or not.
def main():
    print('verbing')
    test(verbing('hail'), 'hailing')
    test(verbing('swiming'), 'swimingly')
    test(verbing('do'), 'do')

    print()
    print('not_bad')
    test(not_bad('This movie is not so bad'), 'This movie is good')
    test(not_bad('This dinner is not that bad!'), 'This dinner is good!')
    test(not_bad('This tea is not hot'), 'This tea is not hot')
    test(not_bad("It's bad yet not"), "It's bad yet not")
    test(not_bad("It's doubleplusbad."), "It's doubleplusbad.")
    test(not_bad("So bad."), "So bad.")


    print()
    print('front_back')
    test(front_back('abcd', 'xy'), 'abxcdy')
    test(front_back('abcde', 'xyz'), 'abcxydez')
    test(front_back('Kitten', 'Donut'), 'KitDontenut')

if __name__ == '__main__':
    main()