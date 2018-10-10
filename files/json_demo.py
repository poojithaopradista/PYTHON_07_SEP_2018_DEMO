import json


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


p = Point(10, 20)
print(json.dumps(p.__dict__))

lp = [Point(10, 20).__dict__, Point(1, 2).__dict__]
print(json.dumps(lp))

jsonperson = '{"name" : "Abc", "mobile": ["39343434","3949343"], "age" : 30}'
person = json.loads(jsonperson)
print(person["mobile"][0])
