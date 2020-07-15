# deque objects are like double ended queues

import collections
import string

def main():
    #initialize a deque with lowercase letters
    d=collections.deque(string.ascii_lowercase)
    print("Item Count:",str(len(d)))

    for elem in d:
        print(elem.upper(),end=",")

    d.pop()
    print(d)
    d.popleft()
    print(d)
    d.append(2)
    print(d)
    d.appendleft(1)
    print(d)

if __name__=="__main__":
    main()

