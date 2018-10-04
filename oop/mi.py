class A:
    def print(self):
        print("print() of A")

    def add(self):
        print("add() of A")


class B(A):
    def print(self):
        print("print() of B")

    def sub(self):
        print("sub() of B")


class C(B,A):
    def print(self):
        print("print() of C")


def fun(v):
    pass


fun(10)
fun("Abc")


obj = C()

print( issubclass(C,B))
print( issubclass(A,B))
print( isinstance(obj,A))

