#Solution to Problem 2
#
#Let it be noted that every third term of the sequence
#is even starting with 2

total=0
f1=2
f2=3
f3=5
while (f1<4000000):
    total+=f1
    f1=f3+f2
    f2=f1+f3
    f3=f2+f1

print(total)
    
