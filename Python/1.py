#1+2+...+n=n*(n+1)/2
#3+6+...+3n=3*n*(n+1)/2
def sumOfSeries(mult,n):
    x=mult*(int(n/mult)*int(n/mult+1)/2)
    return x
threes = summingSeries(3,999)
fives = summingSeries(5,999)
#subtract nums counted twice, aka multiples of 3*5
double_counted=summingSeries(15,999)
print(threes+fives-double_counted)
