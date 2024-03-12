"""
The prime factors of 13195 are 5,7,13 and 29.
What are the largest prime factor of the number 600851475143?
"""

seen = []

def largest_prime_factor(num):
  x = 2
  while num != 1:
    if num % x == 0:
      seen.append(x)
      num /= x
    x += 1
  return 0

largest_prime_factor(600851475143)
print(seen)