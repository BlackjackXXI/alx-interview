#!/usr/bin/python3
"""
Minmum Operations challenge
"""

def minOperations(n):
    """
    Returns the minimum number of operation need
    """
    if n <= 1:
        return 0
    
    operations = 0
    factor = 2

    while n > 1:
        while n % factor == 0:
            operations += factor
            n //= factor
        factor += 1

    return operations

if __name__ == "__main__":
    # Example test cases
    n = 4
    print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

    n = 12
    print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))
