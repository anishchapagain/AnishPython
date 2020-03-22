def one():
    print("one")
    two()

def two():
    print("twoone")
    three()

def three():
    print("onethree")
    four("anish")

def four(var):
    print("onefour")
    print(f'one four: {var}')

if __name__ == "__main__":
    one()
