def main():
    #define a list of days in English and French
    days= ["Sun","Mon","Tue","Wed","Thu","Fri","Sat"]
    daysFr=["Dim","lun","Mar","Mer","Jeu","Ven","Sam"]

    #use iter to create an iterator over a collection
    i=iter(days)
    print(next(i))
    print(next(i))


    #iterator using a function and sentinel
    with open("testfile.txt","r") as f:
        for line in iter (f.readline(),''):
            print(line)


    #use regular interaction over the days
    for m in days:
        print(m)

    #use enumerate reduces code and provides a counter:
    for i,m in enumerate(days,start:=1):
        print(i,m)

    #use zip function to combine sequences
    for m in zip(days,daysFr):
        print(m)

    #combine enumerate and zip
    for i,m  in enumerate(zip(days,daysFr),start=1):
        print(i,m[0],"=",m[1]," in French")


if __name__=="__main__":
    main()