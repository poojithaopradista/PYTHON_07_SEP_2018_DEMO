nums = [10, 20, 11, 33, 44, 90]


def iseven(n):
    return n % 2 == 0


# enums = filter(iseven, nums)
enums = filter(lambda n: n % 2 == 0, nums)

for n in enums:
    print(n)

names = ["Tom", "Larry", "Steve", "Beny"]

for n in sorted(names):
    print(n)

for n in sorted(names, key=lambda n: n[-1]):
    print(n)
