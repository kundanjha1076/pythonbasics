def swap(list):
    get=list[-1],list[0]
    list[0],list[-1]=get
    return list
newlist=[12,23,45,67]
print(swap(newlist))
    