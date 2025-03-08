s=input("Enter the string ")
opstr=""
for i in s:
    if i.isupper():
        o=i.lower()
    elif i.islower():
        o=i.upper()
    else:
        o=i
    opstr+=o
print(opstr)
