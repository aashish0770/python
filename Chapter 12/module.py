def myFun():
    print("Hello from myFun!")


# this is used if we dont want this function to be executed on another file.
# Except this other function will be executed if this file is imported in another file.
if __name__ == "__main__":
    # If this code is directlyy excuted as the main program
    print("This is myFun.py file")
    myFun()
    print(__name__)  # __main__


def myFun2():
    print("Hello from myFun2!")

myFun2()  # this will be executed even if this file is imported in another file.