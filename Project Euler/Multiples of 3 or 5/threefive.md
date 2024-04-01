# Multiples of 3 or 5

## Problem 
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6, 9. The sum of these multiples is 23. Find the sum of all the multiples of 3 or 5 below 1000.

## Approach
When we are looking to find if a number, *x*, is a multiple of some other number, *y*. We can take the modulus of the *x* against the multiple we are seeking to confirm, *y*. This operator for modulus is <code>%</code>

``` python
  x % y
```

## Modulus
A modulus operation is closely related to division. The modulus operation returns the remainder of a division operation. This is useful to know, especially if you are trying to find out whether a *x* is a multiple of *y* because if it is, then the modulus of *x* and *y* would be 0. 

``` python
  answer = 6 % 3
  print(answer) ''' prints 0 '''
```

## What now?
So now we have an way for checking whether a number is a multiple. We can then use this to create conditionals that check whether numbers between 0 and an arbitrary number **n** is a multiple of 3 or 5. 