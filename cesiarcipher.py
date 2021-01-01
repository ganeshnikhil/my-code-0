'''from cryptography.fernet import Fernet
key = Fernet.generate_key()
print(key)
cipher_suite = Fernet(key)
print(cipher_suite)
cipher_text = cipher_suite.encrypt(b"0101110110111")
print(cipher_text)
plain_text = cipher_suite.decrypt(cipher_text)
print(plain_text)'''
'''import hashlib

l = ['MTAwMTAwMTE=']

def check_user(h):
    for i in l:
        if h == hashlib.md5(i.encode('utf-8')).hexdigest():
            print(h)
            return i'''
'''list1=['MTExMDExMTAwMQ==','MTExMDEwMDEwMQ==','MDAxMDEwMDEwMQ==','MDAwMTExMTAwMQ==']
strl=""
c=0
b=16
a=strl.join(list1)
print(a[b:])
print(len(a))'''

'''a=['s','2','i','0','9','a']
a.sort()
print(a)
if len(a)!=len(set(a)):
  print("hello")'''

'''a=['1','2','3','4','5','6']
b=['a','7']
count=0
for i in range(len(b)):
  for j in range(len(a)):
    if b[i] in a[j]:
      count=count+1
if count!=len(b):
  print("not found!")
  print(exit())'''

'''a=input("enter your input=")
a=a[0]
print(a)'''

'''a=['!','@','#','$','%','^','&','*','(',')','_','-','+','=','1','2','3','4','5','6','7','8','9','0','q','w','e','r','t','y','u','i',',',':',';']
a.sort()
print(a)'''
#print(check_user(hashlib.md5(l[0].encode('utf-8')).hexdigest()))