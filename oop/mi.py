class A:
    def print(self):
        print("print() of A")

    def add(self):
        print("add() of A")


class B:
    def print(self):
        print("print() of B")

    def sub(self):
        print("sub() of B")


class C(A, B):
    def print(self):
        super().print()
        print("print() of C")


obj = C()
obj.print()
obj.add()
obj.sub()
