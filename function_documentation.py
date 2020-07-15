#Function Documentation

print(map.__doc__)

import collections
print(collections.__doc__)

#Demonstrate the use of variable argument lists
#Define a function that takes variable arguments

def addition(*args):
    result=0
    for arg in args:
        result+=arg
    return result

def main():
    print(addition(5,10,15,20))
    print(addition(1,2,3))

if __name__=="__main__":
    main()