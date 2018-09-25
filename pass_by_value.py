def change(n):
    print("Address of n before : ", id(n))
    n = 10
    print("Address of n after change : ", id(n))


v = 100
print(id(v))
change(v)
print(v)
