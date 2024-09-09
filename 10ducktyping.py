# pythonic- using python coding style and conventions inorder to write cleana and nice code
# duck typing and concept that is easier to forgivness (eafp)
# we dont care what type of object we are working with we only care what object can do what we want
#so in duck typing we dont care wheather the object is duck type or not but if it quacks like a duck then it is duck type,basically it means that
# if a class or a type is not a duck type but behaves as duck then it is duck typing,we dont care what it is we us care weather he is doing what we want to excecute

class Duck:
    def quack(self):
        print('Quack, quack')
    def fly(self):
        print('Flap, Flap!')
class Person:
    def quack(self):
        print("I'm Quacking Like a Duck!")
    def fly(self):
        print("I'm Flapping my Arms!")
def quack_and_fly(thing):
    if isinstance(thing, Duck): #tells wheather object belongs to class duck or not means instance
        thing.quack()
        thing.fly()
    else:
        print('This has to be a Duck!')
    # LBYL (Non-Pythonic)
    if hasattr(thing, 'quack'): #thismethods tells us wheather the thing object has attritube or not 
        if callable(thing.quack):
            thing.quack()

    if hasattr(thing, 'fly'):
        if callable(thing.fly):
            thing.fly()
    # EAFP (Pythonic)
    try:
        thing.quack()
        thing.fly()
        thing.bark()
    except AttributeError as e:
            print(e)
d=Duck()
print(type(d))
print(type(dir(d)))