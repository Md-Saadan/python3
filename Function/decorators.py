def greetings(func):
    def wrapper():
        print("Welcome to the class")
        func()
        print("Thanks!")
    return wrapper

@greetings
def morning():
    print("Good Morning!")
morning()

@greetings
def evening():
    print("Good Evening!")
evening()

