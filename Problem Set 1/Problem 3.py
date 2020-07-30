# Assume s is a string of lower case characters.

# Write a program that prints the longest substring of s in which the letters occur in alphabetical order. 
# For example, if s = 'azcbobobegghakl', then your program should print

# Longest substring in alphabetical order is: beggh
# In the case of ties, print the first substring. For example, if s = 'abcbcd', 
# then your program should print:

# Longest substring in alphabetical order is: abc

s = 'azcbobobegghakl'
longest = s[0]
current = s[0]
for i in s[1:]:
    if i >= current[-1]:
        current += i
        if len(current) > len(longest):
            longest = current
    else:
        current = i
print('Longest substring in alphabetical order is: ', longest)