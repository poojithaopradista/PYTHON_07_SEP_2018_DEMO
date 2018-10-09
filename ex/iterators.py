class EvenNumbers:
    def __init__(self, start, end):
        self.start = start if start % 2 == 0 else start + 1
        self.end = end

    def __iter__(self):
        self.number = self.start
        return self

    def __next__(self):
        if self.number <= self.end:
            num = self.number
            self.number += 2
            return num
        else:
            raise StopIteration


# Generator to generate even numbers from start to end
def even_numbers(start, end):
    start = start if start % 2 == 0 else start + 1
    end = end + 1 if end % 2 == 0 else end
    for n in range(start, end, 2):
        yield n


en = even_numbers(10, 20)

for n in en:
    print(n)
