from collections import defaultdict

my_string="""3
1 PT
2 US
3 PT
3
1 1 10
2 1 7
3 2 10
4 3 4"""

my_string= my_string.split("\n")


user=my_string[1:1+int(my_string[0])]
task=my_string[2+int(my_string[0]):]

user_av_dict=defaultdict(list)
country_av_dict=defaultdict(list)

for i in range(0,len(user)):
    usery=user[i].split()
    for j in range(0,len(task)):
        tasky=task[j].split()
        if int(tasky[1]) == int(usery[0]):
            user_av_dict[usery[0]].append(int(tasky[2]))
            country_av_dict[usery[1]].append(int(tasky[2]))

for k,i in user_av_dict.items():
    print(k,sum(i)/len(i))
    
for k,i in country_av_dict.items():
    print(k,sum(i)/len(i))

