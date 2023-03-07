class Emp:
    def __int__(self, id, name):
        self.id = id
        self.name = name

    def show(self):
        print(self.id, self.name)


a = Emp(1, "aka")

print(a.show())
