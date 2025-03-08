n=int(input('Number of days'))
stock=[]
print('The stock values are')
for i in range(n):
    l=float(input())
    stock.append(l)
minSoFar=float('inf')
maxProfit=0
for i in stock:
    minSoFar=min(minSoFar,i)
    maxProfit=max(maxProfit,i-minSoFar)
print(maxProfit)
