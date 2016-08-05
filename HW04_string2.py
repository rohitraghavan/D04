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
def verbing(s):
    strlen = len(s)
    newstring = s
    if strlen >= 3:
        #If last 3 chars of a string with length >=3 end in ing, append ly, else append ing
        if s[-3:] == 'ing':
            newstring = s + "ly"
        else:
            newstring = s + "ing"
    return newstring


# E. not_bad
# Given a string, find the first appearance of the
# substring 'not' and 'bad'. If the 'bad' follows
# the 'not', replace the whole 'not'...'bad' substring
# with 'good'.
# Return the resulting string.
# So 'This dinner is not that bad!' yields:
# This dinner is good!
def not_bad(s):
    newstring = s
    #Find positions of not and bad
    notposition = s.find("not")
    badposition = s.find("bad")
    #If both not and bad are found, and not comes before bad, then replace not..bad with good.
    if notposition != 1 and badposition != 1 and notposition < badposition:
        newstring = s[0:notposition] + "good" + s[badposition+3:]

    return newstring


# F. front_back
# Consider dividing a string into two halves.
# If the length is even, the front and back halves are the same length.
# If the length is odd, we'll say that the extra char goes in the front half.
# e.g. 'abcde', the front half is 'abc', the back half 'de'.
# Given 2 strings, a and b, return a string of the form
#  a-front + b-front + a-back + b-back
def front_back(a, b):
    #Handle even length string a
    if len(a) % 2 == 0:
        splitlength = int(len(a) / 2)
    #Handle odd length string a
    else:
        splitlength = int(len(a) / 2) + 1
    #Split string a
    afronthalf = a[:splitlength]
    abackhalf = a[splitlength:]
    
    #Handle even length string b
    if len(b) % 2 == 0:
        splitlength = int(len(b) / 2)
    #Handle odd length string b
    else:
        splitlength = int(len(b) / 2) + 1
    #Split string b
    bfronthalf = b[:splitlength]
    bbackhalf = b[splitlength:]
    
    return afronthalf + bfronthalf + abackhalf + bbackhalf


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
    test(not_bad('This movie is not so bad huh'), 'This movie is good huh')
    test(not_bad('This dinner is not that bad!'), 'This dinner is good!')
    test(not_bad('This tea is not hot'), 'This tea is not hot')
    test(not_bad("It's bad yet not"), "It's bad yet not")

    print()
    print('front_back')
    test(front_back('abcd', 'xy'), 'abxcdy')
    test(front_back('abcde', 'xyz'), 'abcxydez')
    test(front_back('Kitten', 'Donut'), 'KitDontenut')

if __name__ == '__main__':
    main()
