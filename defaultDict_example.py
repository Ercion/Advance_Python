#Demonstrate the usage of defaultDict objects

from collections import defaultdict

def main():
    fruits=['apple','pear','orange','banana','apple','grape','banana','banana']

    fruitCounter=defaultdict(lambda :100)

    for fruit in fruits:
        fruitCounter[fruit]+=1

    for k,v in fruitCounter.items():
        print(k+":"+str(v))

    if __name__=="__main":
        main()

