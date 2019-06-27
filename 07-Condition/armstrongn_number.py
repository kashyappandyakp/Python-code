num = int(input("Enter Any Number: "))

sum = 0

temp = num 
while temp > 0 :
    digit = temp % 10 
    sum += digit ** 3
    
if num == sum:
    print(num,"Is an Armstrong Number")
else:
    print(num,"IS not an Armstrong Number")
    