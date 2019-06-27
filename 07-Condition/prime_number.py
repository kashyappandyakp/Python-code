num = int(input('Enter Any Number: '))

if num > 1:

    result=True

    for i in range(2, num):
        if num % i == 0:
            print(i,"times",num//i,"is",num)
            result=False
            break 
else:
    print(num,"is not a prime number")
    
if  result:
    print("{} is prime".format(num))
else:
    print("{} is not a prime".format(num))