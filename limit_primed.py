lower = 900
upper = 1000
for n in range(lower,upper+1):
    for i in range(2,n):
        if (n % i ) ==0:
            break
    else:
        print(n)
    
