
s = 'mypassword'
t1 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890abcdefghijklmnopqrstuvwxyz'
t2 = 'IJKLMNOPQRSTUVWXYZopqrstuvwxyzA1B2C3D4E5F6G7H890abcdefghijklmn'
for i in range(len(s)):
 p = t1.find(s[i])
 s = s[:i]+t2[p]+s[i+1:]

print(s) #amdDggkcf5
for i in range(len(s)):
 p = t2.find(s[i])
 s = s[:i]+t1[p]+s[i+1:]
print(s)
