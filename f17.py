#the number of digitts
num=abs(int(input('enter the number')))
digits = 1
while(num>9):
    num = num // 10
    digits = digits + 1 
print(digits)

