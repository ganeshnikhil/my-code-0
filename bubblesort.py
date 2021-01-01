a=int(input("enter the lenght of list="))
list1=[]
for i in range(a):
    b=int(input("enter  the number in list="))
    list1.append(b)
for i in range(b):
    for j in range(a-i-1):
        if list1[j]>list1[j+1]:
            list1[j],list1[j+1]=list1[j+1],list1[j]
print("sorted list=",list1)