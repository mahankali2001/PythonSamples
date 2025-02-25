# Bit Manipulation: Determine if an integer is a power of two.

def isPowerOfTwo(n: int) -> bool:
    return n > 0 and n & (n - 1) == 0

print(isPowerOfTwo(16))