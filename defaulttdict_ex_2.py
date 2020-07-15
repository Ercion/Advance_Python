from collections import  defaultdict

def groupby_owners(files):
    my_files=defaultdict(list)

    for key,value in files.items():
        if value!=None:
            my_files[value].append(key)
        
    return  my_files
    


if __name__=="__main__":
    files={"input.txt":"Randy",
           "Code.py":"Stan",
           "Output.txt":"Randy"
           }
    print(groupby_owners(files))