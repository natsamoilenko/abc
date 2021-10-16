a = [3,5,2,77, 88]

#print( 5 not in a)
#print( 6 not in a)

b = 7 
if b not in a:
    a.append(b)

print (a)

s = 0
i = 0 
while i < len(a):
    s = s+a[i]
    i = i+1
print(s)

s = 0 

for x in a:
    s = s+x
    
print(s)
    
s = 0

for i in range(0,len(a)):
    print(i)
    s = s+a[i]
print(s)

c = []

