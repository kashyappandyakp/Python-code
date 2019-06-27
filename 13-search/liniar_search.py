def search(L1, key):
    result=False
    
    for i in L1:
        if i==key:
            result = True
            break
    return result
L1 = [1,2,3,4,5,6,7,26,65,3,5]
key = int(input("Enter any Number: "))

if search(L1, key):
    print("Found")
else:
    print("Not found ")