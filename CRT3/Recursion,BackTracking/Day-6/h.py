'''a=10
b=20
a,b = b,a
print(a)
print(b)

a=10
b=20
a=a-b
b=a+b
a=b-a
print(a)
print(b)

 
a = 5
b = 10
a = a ^ b
b = a ^ b
a = a ^ b
print(a)
print(b)   
  
num="5320100" 
num=num[::-1]
print(num)
s=int(num)
print(s)
k=str(s)
print(s)
k=k[::-1]
print(k)
            
'''
     
word1 = "abc"
word2 = "pqr"
r = ""

for i in range(len(word1)):
    r += word1[i] + word2[i]

print(r)
