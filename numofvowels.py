string=input()
vowel=["a","e","i","o","u","A","E","I","O","U"]
flag=0
for i in range(len(string)):
    if(string[i] in vowel):
        flag+=1
if(flag==0):
    print("No vowels were found.")
else:
    print("Total number of vowels:",flag)
    
