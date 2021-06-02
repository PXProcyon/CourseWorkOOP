class Tree():

    def __init__(self, kind, height):
        self.kind = kind
        self.age = 0
        self.height = height

    def info(self):
        print("{} years old {}. {} meters high.".format(self.age, self.kind, self.height))

    def grow(self):
        self.age += 1
        self.height += 0.5

    def extragrow(self):
        exgrow = self.height.__add__(self.height)
        print("{} years old {}. {} meters high.".format(self.age, self.kind, exgrow))

t1 = Tree("Oak",10)
t1.info()
t1.grow()
t1.info()
t1.extragrow()
