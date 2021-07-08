a=[]
b=int(input("enter the length of list"))
for i in range(b):
    a=a+[int(input("enter any number"))]
key=int(input("enter any number to search"))
l=0
a.sort()
flag=0
h=(len(a)-1)
while (h-1)>1:
    mid=(l+h)//2
    if a[mid]==key:
        flag=1
        print("element is found")
        break
    elif key>a[mid]:
        l=mid+1
    elif key<a[mid]:
        h=mid-1
if a[h]==key or a[l]==key:
    print("element is found")
    flag=1
if flag==0:
    print("Element is not found in list")