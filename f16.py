#ques on while loop
print('enter a number')
n=int(input())
i=1
if(n>0):
    while(n>0):
        i=i*n
        n=n-1
    print(i)
else:
    print('not defined')
    