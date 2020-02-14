n= int(input())
l=[],m=[],n=[]
for i in range(n):
  x=int(input())
  l.append(x)
m=l.reverse()
for i in range(n):
  n.append([i]+m[i])
print(n)
