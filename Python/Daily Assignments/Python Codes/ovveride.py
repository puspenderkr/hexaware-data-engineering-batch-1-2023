class Bird:
    #constructor
    def __init__(self,name):
        self.name = name

    def print_info(self):
        print('This bird is', self.name)

    def fly(self):
        print('the bird can fly')

# parrot class inherits from Bird class with all attr ibutes.

class Shalik(Bird):

    def __init__(self, name, color, charater):

        #call the constructor of parent class
        super().__init___(name)
        self.color = color
        self.charater = charater


    #Override method
    def print_info(self):
        #call the method of parent class
        super().print_info()

        print('color of bird is', self.color)

        print('Character of bird is', self.charater)


    #override method
    def fly(self):
        print('the bird can fly')

obj_Shalik =  Shalik('Shalik', 'black', 'not good')

obj_Shalik.fly()

Shalik.print_info()
    