with open(r"..\customers.txt", "rt") as f:
    customers = {}
    for line in f.readlines():
        details = line.split(",")
        if len(details) < 2:
            continue

        # check whether mobile number is valid
        name = details[0]
        mobile = details[1].strip("\n")
        if not(len(mobile) == 10 and mobile.isdigit()):
            continue

        if not (name.isalpha() or name.isspace()):
            continue

        customers[name] = mobile

# print

for n,m in sorted(customers.items()):
    print("%-20s  %s" % (n,m))
