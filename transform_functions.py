##Demonstrate the usage of transform functions like sorted,filter and map

def filterFunc(x):
    if x%2==0:
        return False
    return True

def FilterFunc2(x):
    if x.isupper():
        return False
    return True

def squareFunc(x):
    return x**2

def toGrade(x):
    if x >=90:
        return "A"
    elif x >=80 and x< 90:
        return "B"
    elif  x>=65 and x<70:
        return "D"
    return "F"


def main():
    #define some sample sequences to operate on
    nums=(1,8,4,5,13,26,282,410,342,47)
    chars="abcDefGHijklmnoPR"
    grades=(81,90,94,78,61,66,99,47)

    #use filter to remove items from a list
    lowers=list(filter(filterFunc,nums))
    print(lowers)

    #use map to create a new sequence of values
    squares=list(map(squareFunc,nums))
    print(squares)

    #use sorted and map to change numbers to grades
    grades=sorted(grades)
    letters=list(map(toGrade,grades))
    print(letters)


if __name__=="__main__":
    main()