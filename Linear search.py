a=int(input("enter length of list"))
l=[]
for i in range(a):
    l=l+[int(input("enter any number"))]
print(l)
key=int(input("enter any number to search"))
flag=0
for i in range(a):
    if l[i]==key:
        print("element is found at",i)
        flag=1
        break
if flag==0:
    print("element is not found in the list")