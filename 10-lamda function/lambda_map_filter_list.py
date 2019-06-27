#lambda function with filter 

import math

a = [25,2,12,10,11,14,15,12,13,10,22,55,44,95,36,18,91,95,94,41,71,46,]
f = list(filter(lambda x:(x % 2 == 0), a))
print(f)

