n=int(input())
l=[]
for i in range(n):
    element=int(input())
    l.append(element)
tsum=sum(l)
average=tsum/n
print("The average is: {:.2f}".format(average))
