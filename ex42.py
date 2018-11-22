#python3.6 ex42.py
## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
# default animal size is 5
    def __init__(self, size = 5):
        self.size = size

    def walk_on_4(self):
        print("This animal is walkin' on 4 legs!")

## Dog is-a Animal
class Dog(Animal):
# Dog has-a __init__ that takes self and name parameters
    def __init__(self, name):
        self.name = name

    def bark(self):
        print("Bark! Bark! Woof! Woof!")

## Cat is-a Animal
class Cat(Animal):

    def __init__(self, name, fur_style):
        #Cat has-a init with parameters self and name
        self.name = name
        self.fur_style = fur_style
        self.pet = None
        super(Cat, self).__init__()

    def groom(self):
        print(f"The cat wets and grooms its {self.fur_style} fur.")
        #def shrink():
            #print("The cat shrinks!")
            #Cat.size -= -1
            #print(Cat.size)

## Person is-a object
class Person(object):

    def __init__(self, name, balding):
        # Person has-a __init__ that takes self and name
        self.name = name
        self.balding = balding
        ## Person has-a pet of some kind
        self.pet = None

## Employee is-a Person
class Employee(Person):

    def __init__(self, name, salary, balding):
        ## super() can be used to gain acess to inherited methods from parent or sibling class
        # this makes Employee a sublcass of Person! i.e. it inherits stuff from person (name)
        super(Employee, self).__init__(name, balding)
        ## the attribute salary is part of the employee class...
        self.salary = salary

## Fish is-a object
class Fish(object):
    def __init__(self, scales=True, gills=True, edible=None, genus = None):
        self.scales = scales
        self.gills = gills
        self.edible = edible
        self.genus = genus

    def swim(self):
        print("Swim, swim, swim, I'm a fish!")


## salmon is-a fish...
class Salmon(Fish):
    pass

## Halibut is-a fish
class Halibut(Fish):
    pass

## rover is-a Dog
rover = Dog("Rover")

## satan is-a cat
satan = Cat("Satan", "fluffy")

## mary is-a person
mary = Person("Mary", "not bald")

## mary's pet is satan?
mary.pet = satan

## frank is-a employee, frank has-a salary of 120000
frank = Employee("Frank", 120000, "bald")

## frank's pet is-a dog is-a rover
frank.pet = rover

## flipper is-a Fish
flipper = Fish()

## crouse is-a Salmon
crouse = Salmon()

## ??
harry = Halibut()


print(satan.size)
print(satan.name)
print(satan.fur_style)
satan.groom()

print("Franks stuff:")
print(frank.name)
print(frank.salary)
print(f'If there\'s no hair on {frank.name}\'s head, then he\'s {frank.balding}')

print("MARY!")
print(mary.balding)
