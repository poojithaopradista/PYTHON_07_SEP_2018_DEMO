
f = open(r"..\names.txt")

names = set()
for line in f:
    parts = line.strip("\n").split(",")
    for name in parts:
        names.add(name)

for n in sorted(names):
    print(n)

