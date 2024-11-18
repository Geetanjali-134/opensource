m=input().split()
flag=0
if len(m[0])==3 and m[0][0]=='+':
    for i in m[1]:
        if(i.isdigit()):
            flag=1
            continue
        else:
            flag=0
if flag==0:
    print("Incorrect")
else:
    print("Correct")
