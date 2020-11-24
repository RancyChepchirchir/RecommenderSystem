import matplotlib.pyplot as plt
import numpy as np 
import matplotlib.ticker as ticker

a1 = [[1, 1, 1, 1, 1, 0, 0, 1, 1, 1],
[1, 1, 1, 1, 1, 1, 0, 1, 0, 1],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[1, 1, 1, 0, 1, 0, 1, 1, 0, 1],
[1, 1, 1, 1, 0, 1, 0, 1, 1, 0],
[0, 1, 1, 0, 1, 0, 0, 1, 0, 1],
[1, 1, 1, 1, 0, 0, 1, 0, 1, 0],
[1, 0, 1, 1, 1, 1, 1, 0, 1, 1],
[1, 1, 1, 1, 1, 0, 0, 0, 1, 1],
[1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
[1, 1, 0, 0, 0, 0, 1, 1, 0, 1],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[1, 1, 1, 1, 1, 1, 0, 1, 1, 0],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[1, 1, 1, 1, 1, 1, 1, 1, 0, 1],

[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],        #Sahaj's values are left
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

def MAP(doc):
    sum = 0
    s = 0
    for i, item in enumerate(doc):
        sum += doc[i]
                 #Finish code for MAP
    s = (float(float(sum)/(10)))
    return s#, array

y_arr = []
s_arr = 0

for j in range(24):
    s_arr += MAP(a1[j])
    y_arr += [MAP(a1[j])]

print (float(s_arr)/(24))
plt.plot(range(1, 25), y_arr)                 #y_arr has to be changed
plt.xlabel("No. of queried documents")
plt.ylabel("Precision@10")
plt.show()