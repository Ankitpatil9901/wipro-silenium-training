# decorators - wrapper function around the functions are called decorators
# decorator method


def make_prett(func):
    def inner():
        print("I got decorated")
        func()
    return inner

@make_prett
def vanillacake():
    print(" I am Venilla cake")

@make_prett
def straberrycake():
    print("I am strawberry cake")

vanillacake()
straberrycake()