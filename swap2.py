def swap(List,pos1,pos2):
    List[pos1],List[pos2]=List[pos2],List[pos1]
    return List
List = [23,65,19,90]
pos1,pos2=1,3
print(swap(List,pos1,pos2))