"""
Task

You get an array of numbers, return the sum of all of the positives ones.

Example [1,-4,7,12] => 1 + 7 + 12 = 20

Note: if there is nothing to sum, the sum is default to 0.
"""

def positive_sum(arr):
    a = 0
    for x in range(len(arr)):
        if arr[x] > 0:
            a += arr[x]
    return a


"""
best solution

def positive_sum(arr):
    return sum(x for x in arr if x > 0)

"""

