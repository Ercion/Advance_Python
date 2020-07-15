def main():
    #use any() and all() to testsequences for boolean values
    list1=[1,2,3,0,5,6]
    print(any(list1)) #True
    print(all(list1)) #False Because of 0 value
    print(min(list1))
    print(max(list1))
    print(sum(list1))

if __name__=="__main__":
    main()