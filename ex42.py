#python 3.6 ex42.py

#Animal is-a object
class Animal(object):
  
  def __init__(self, size):
    self.size = size
  
  def walk_on_4(): 
    print("This animal is walkin' on 4 legs!")
## Dog is-a Animal
class Dog(Animal):

  def __init__(self, name):
    self.name = name
  
  def bark():
    print("Bark! Bark! Woof! Woof!")
## Cat is-a Animal
class Cat(Animal):
# Cat has-a init with self, name and fur parameters
  def __init__(self, name, fur):
    self.name = name
    self.fur = fur
    self.pet = None
  
  def groom():
    print(f"the cat wets and grooms its {fur} fur")
# not sure if this works, just testing to see if I can pull from Animals  
  def shrink():
    print("The cat shrinks!")
    Cat.size -= -1
    print(Cat.size)
    
class Person(object):

  def __init__(self, name):

    self.name = name
    self.pet = None

class Employee(Person):

  def __init__(self, name, salary):
    super(Employee, self).__init__(name)

    self.salary = salary
