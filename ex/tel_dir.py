phones = {}

while True:
    name = input("Enter customer name : ")
    if name == "end":
        break

    phone = input("Enter phone number :")
    if name in phones:  # name is already present
        phones[name].add(phone)
    else:  # add new name
        phones[name] = {phone}    # put name and set with one phone number


for n,pl in sorted(phones.items()):
    print("%-20s %s" % (n, ",".join(pl)))


