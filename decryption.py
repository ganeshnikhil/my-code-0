encrypted_list=['MTAwMTAwMTE=', 'MDAwMDAwMDEwMQ==', 'MDEwMTAwMTE=']
import base64
final=[]
final_end=[]
decoded_list=[]
encrypted_main=[]
position_list=[]
process_list=[]
for i in range(len(encrypted_list)):
   b1 = encrypted_list[i].encode("UTF-8")
   final.append(b1)
# Decoding the Base64 bytes
for i in range(len(final)):
  d = base64.b64decode(final[i])
  final_end.append(d)
# Decoding the bytes to string
for i in range(len(final_end)):
  s2 = final_end[i].decode("UTF-8")
  decoded_list.append(s2)
print(decoded_list)


reverse_list=[j[::-1]for j in decoded_list]
print(reverse_list)

for i in range(len(reverse_list)):
    reverse_list[i]=int(reverse_list[i],2)
print(reverse_list)

for i in range(len(reverse_list)):
    c=reverse_list[i]//10
    e=reverse_list[i]%10
    encrypted_main.append(c)
    position_list.append(e)
print("orignal use for decryption:",encrypted_main)
print("position of decrypted cipher:",position_list)

for i in range(len(encrypted_main)):
    for j in range(1,27):
        if encrypted_main[i]%j==0:
            t=encrypted_main[i]/j
            if t<26 and j<26 and j>=t:
                process_list.append(j)
                process_list.append(t)
                print(process_list)
