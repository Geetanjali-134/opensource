n=int(input())
s=0
while n>0:
    a=n%10
    n//=10
    s+=a
if s%2==0:
    print("Vignesh")
else:
    print("Charan")
