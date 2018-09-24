def add(n1, n2):
    return n1 + n2


def sub(n1, n2):
    return n1 - n2


def operation(n1, n2, op):
    print(op(n1, n2))


operation(10, 20, lambda n1, n2: n1 + n2)
operation(50, 40, lambda n1, n2: n1 * n2)
operation(50, 40, sub)
