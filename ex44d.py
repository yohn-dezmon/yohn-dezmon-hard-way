class Parent(object): # creates a class called Parent

    def override(self): # defines the override function
        print("PARENT override()")

    def implicit(self): #
        print("PARENT implicit()")

    def altered(self): #
        print("PARENT altered()")

class Child(Parent): # Child is-a Parent class

    def override(self): # overwriting the override function, i.e. using the same name but printing
    # something distinct.
        print("CHILD override()")

    def altered(self): # overwriting altered
        print("CHILD, BEFORE PARENT altered()")
        super(Child, self).altered() # this calls the Parent altered function
        print("CHILD, AFTER PARENT altered()")

dad = Parent() # instantiates the parent class with object 'dad'
son = Child() # instantiates child class with object 'son'

dad.implicit() # calls the implicit method from the parent class
son.implicit() # calls the implicit method from the parent class

dad.override() # calls the override method from the Parent class
son.override() # calls the override method from the child class

dad.altered() # calls the altered method from the Parent class (check)
son.altered() # prints a distinct statement, calls the parent altered function, then
# prints another distinct statement 
