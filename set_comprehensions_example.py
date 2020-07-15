#Demonstrate how to use set comprehensions
def main():
    #define a list of temperature data points
    ctemps=[5,10,12,14,10,23,41,30,12,18,29]
    ftemps1=[(t*9/5)+32 for t in ctemps]
    print(ftemps1)

    #build a set from an input source

    sTemps="The quick brown fox over the lazy dog"

    chars={c.upper() for c in sTemps if not c.isspace()}
    print(chars)

if __name__=="__main__":
    main()