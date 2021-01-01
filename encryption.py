import pandas as pd 
import base64

main_list=['0','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','0','1','2','3','4','5','6','7','8','9']
input_list=[]
position_list=[]
position_main=[]
final_encrypted_list=[]


lenght=int(input("enter the lenght of string="))
for i in range(lenght):
    input1=input("enter your plan password one by one:")
    input1=input1[0]
    input_list.append(input1)
print("given input:",input_list)
 

 #if you repeat a string in your input then this part of code will excute.
if len(input_list)!=len(set(input_list)):
    print("may be you are repeating the same string!")
    print(exit())


input_conversion=pd.Series(input_list)
input_conversion=list(input_conversion)
input_conversion.sort()
print("sorted list:",input_conversion)

for j in range(len(input_conversion)):
    for k in range(len(input_conversion)):
        if input_conversion[k]==input_list[j]:
            position_list.append(k)
print("position of input:",position_list)
  


# if your input is not found in main_list .
count=0
for i in range(len(input_list)):
  for j in range(len(main_list)):
    if input_list[i] in main_list[j]:
      count=count+1
#this logic will excute.
if count!=len(input_list):
  print(" input not found!")
  print("main list=",main_list)
  print(exit())
   



for m in range(len(input_list)):
    for n in range(1,len(main_list)):
        if input_list[m]==main_list[n]:
            position_main.append(n)
print("position of alphabet input:",position_main)
 

position_conversion=pd.Series(position_main)
descen_list=position_conversion.sort_values(ascending=False)
ascen_list=position_conversion.sort_values(ascending=True)

descen_list=list(descen_list)
print("position of input in descending:",descen_list)
ascen_list=list(ascen_list)
print("position of input in descending:",ascen_list)


print("ascend list * descen list+ position list:")
for l in range(len(ascen_list)):
    if position_list[l]>9:
        a=descen_list[l]*ascen_list[l]*pow(10,2)+position_list[l]
        print("[",a,",","]",end="")
        final_encrypted_list.append(bin(a)[2:])
    else:
        a=descen_list[l]*ascen_list[l]*pow(10,1)+position_list[l]
        print("[",a,",","]",end="")
        final_encrypted_list.append(bin(a)[2:])
print("\n binary list:",final_encrypted_list)



reverse_list=[j[::-1]for j in final_encrypted_list]
print("reverse binary:",reverse_list)


empty=[]
second=[]
final_encryption=[]
final_join=""
for i in range(len(reverse_list)):
    b=reverse_list[i].encode("UTF-8")
    empty.append(b)

for i in range(len(empty)):
    e=base64.b64encode(empty[i])
    second.append(e)


for i in range(len(second)):
    s1=second[i].decode("UTF-8")
    final_encryption.append(s1)
print("Base64 Encoded:",final_encryption)
print("final part of encryption:",final_join.join(final_encryption))