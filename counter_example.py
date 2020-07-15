from collections import Counter


def main():
    class1=["Bob","Becky","James","Melanie"]
    class2=["Bill","James","Taraa","Ziggy"]

    #Create a Counter for Class1  Class2
    c1 = Counter(class1)
    c2 = Counter(class2)

    #How many students in class1 named James ?
    print(c1["James"])

    #How many students are in class1?
    print(sum(c1.values()),"student in class1")

    #Combine the two classes
    c1.update(class2)
    print(sum(c1.values()), "student in class1")

    #What is the most common name in the classes?
    print(c1.most_common(3))

    #seperate the classes again
    c1.subtract(class2)
    print(c1.most_common(3))

    #what is the common between the two classes
    print(c1&c2)


if __name__=="__main__":
    main()