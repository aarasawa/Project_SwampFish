"""
A palindromic number reads the same both ways. Largest palindrome made from the product 
of two 2-digit numbers is 9009 = 91 x 99.

Find the largest palindrome made from the product of 2 3-digit numbers.
"""
lst = []
for x in range(100, 999):
  for y in range(100, 999):
    prod = str(x * y)
    rev = ''.join(reversed(prod))
    if prod == rev:
      lst.append(x * y)
print(max(lst))