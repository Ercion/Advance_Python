#Demonstrate the usage of OrderedDict objects

# colections This module implements specialized container datatypes providing alternatives to Python's general purpose built-in containers, dict,list,set and tuple

from collections import OrderedDict

def main():
    sportTeams=[("Royals",(18,12)),("Rocket",(24,26)),("Dragons",(22,8)),("Kings",(15,15))]

    #Sorted Teams
    sortedTeams=sorted(sportTeams, key=lambda t:t[1][0],reverse=True)  # sort the teams by number of wins

    #create an ordered dictionary of the teams
    teams=OrderedDict(sortedTeams)
    print(teams)

    #use popitem to remove the top item
    team,winlose = teams.popitem(False) #false give the top, True gives last
    print("top team",team,winlose)

    #what are next the top 3 teams?
    for i,team in enumerate(team,start=1):
        print(i,team)
        if i==3:
            break

    #test for equality
    a=OrderedDict({"a":1,"b":2})  #they must have same order!
    b=OrderedDict({"a":1,"b": 2})
    print("Equality Test",a==b)


if __name__=="__main__":
    main()