#!/usr/bin/python3
str = "Python is an interpreted, interactive, object-oriented programming language that combines remarkable power with very clear syntax"
# the output is built from three slices of str joined with plus signs
# first object-oriented programming, then with, then the first word
print(str[39:67] + str[107:112] + str[:6])
