# Checks whether a number is prime

import sys

if len(sys.argv) < 2:
    print("Usage : python prime.py number")
    sys.exit(0)  # Terminate program


num = int(sys.argv[1])

for n in range(2, num//2 + 1):
    if num % n == 0:
        print(num, "is not prime number!")
        break
else:
    print(num, "is prime number!")


