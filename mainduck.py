# a = 3
# b = "tim"
# c = 4.7
#
# print(a)
# print(b)
# print(c)

class Wing(object):

    def __init__(self, ratio):
        self.ratio = ratio

    def fly(self):
        if self.ratio > 1:
            print("Whee this is fun")
        elif self.ratio == 1:
            print("This is difficult, but I'm flying")
        else:
            print("I think I'll just walk")


class Duck(object):

    def __init__(self):
        self._wing = Wing(1.8)


    def walk(self):
        print("Waddle, waddle")

    def swim(self):
        print("Come on in")

    def quack(self):
        print("Quack, quack")

    def fly(self):
        self._wing.fly()

class Penguin(object):

    def walk(self):
        print("I waddle to")

    def swim(self):
        print("Come on in to the cold, cold water.")

    def quack(self):
        print("I'm not a duck you tosser.")

# def test_duck(duck):
#     duck.walk()
#     duck.swim()
#     duck.quack()


if __name__ == '__main__':

    donald = Duck()
    donald.fly()
    #
    # percy = Penguin()
    # test_duck(percy)
