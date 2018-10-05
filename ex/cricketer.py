from abc import ABC, abstractmethod

# Abstract class
class Cricketer(ABC):
    def __init__(self, name, country):
        self.name = name
        self.country = country

    @abstractmethod
    def get_points(self):
        pass

    def print(self):
        print("Name      : ", self.name)
        print("Country   : ", self.country)


class Batsman(Cricketer):
    def __init__(self, name, country, runs):
        Cricketer.__init__(self, name, country)  # super().__init__(name,country)
        self.runs = runs

    def print(self):
        Cricketer.print(self)
        print("Runs      : ", self.runs)

    def get_points(self):
        return self.runs // 100


class Bowler(Cricketer):
    def __init__(self, name, country, wickets):
        Cricketer.__init__(self, name, country)
        self.wickets = wickets

    def print(self):
        Cricketer.print(self)
        print("Wickets   : ", self.wickets)

    def get_points(self):
        return self.wickets // 5


class Allrounder(Batsman, Bowler):
    def __init__(self, name, country, runs, wickets):
        Batsman.__init__(self, name, country, runs)
        Bowler.__init__(self, name, country, wickets)

    def print(self):
        Batsman.print(self)
        print("Wickets   : ", self.wickets)

    def get_points(self):
        return Batsman.get_points(self) + Bowler.get_points(self)


a = Allrounder("Kapil", "India", 6700, 410)
a.print()
print(a.get_points())
