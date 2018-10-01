class Time:
    def __init__(self, h=0, m=0, s=0):
        self.hours = h
        self.mins = m
        self.secs = s

    def total_seconds(self):
        return self.hours * 3600 + self.mins * 60 + self.secs

    def __str__(self):
        return "%02d:%02d:%02d" % (self.hours, self.mins, self.secs)

    def __eq__(self, other):
        print("__eq__")
        return self.total_seconds() == other.total_seconds()

    def __gt__(self, other):
        print("__gt__")
        return self.total_seconds() > other.total_seconds()

    def __add__(self, other):
        pass

    def print(self):
        print("%02d:%02d:%02d" % (self.hours, self.mins, self.secs))

    def set_hours(self, hours):
        if hours < 0 or hours > 23:
            raise ValueError("Invalid Hour")
        else:
            self.hours = hours

    def is_valid(self):
        if self.hours >= 0 and self.hours <= 23 \
                and self.mins >= 0 and self.mins <= 59 \
                and self.secs >= 0 and self.secs <= 59:
            return True
        else:
            return False


t1 = Time(10, 20, 30)
t2 = Time(10, 20, 30)
t3 = Time(1, 2, 3)
print(t1 == t2)
print(t1 > t3)  # __gt__(t1,t3)
print(t1 < t3)
print(t1 != t3)
print(t1)  # str(t1)  -> t1.__str__()
print(str(t1))
print(t1.__str__())

ts = int(t1)