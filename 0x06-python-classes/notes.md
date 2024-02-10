procedure oriented programming : 


# oop

# classes and objects:
 are two main aspects of oop, a class creates a new type where objects are instances of class.

 * objects : can store data using ordinary variables that belong to the object, variables that belong to an object or class are reffered to as fields. 
 * objects also have functionality by using functions that belong to a class such functions are called methods of a class. collectively the fields and methods can be reffered to as the attributes of that class.
    * fields are two types- they can belong to instance/object of class or they belong to the class iitself aka instance variables and class variables

    * class methids have only one difference from ordinary functions that is they must have extra first name that has to be added to beginning parameterlist. this variable parameter is [(self)] 

* classses: class Person:
                pass
            p = Person()
            print(p)
* method:   class Person:
                def say_hi(self):
                    print('Hello ,)

            p = Person()
            p.say_hi()