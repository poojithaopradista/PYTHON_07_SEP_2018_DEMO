def even_numbers():
    for n in range(2, 11, 2):
        yield n


g = even_numbers()
print(type(g))

print(next(g), next(g))

for n in even_numbers():
    print(n)
