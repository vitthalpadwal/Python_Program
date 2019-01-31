print(pow(2,8))

print(max(1,2,4,1,3,6))
print(min(1,2,4,1,3,6))
print(2**3)
print(22/7)

s = 'hellow #world'
t='hellow #world'
print(s in t)
print(id(s),id(t))

a=2
b=5
a,b=b,a

s1 = "hello world grow"
print(s.find('o',5))
print(s.count('o'))

for i in s:
    print(i)

for i in range(0,3):
    print(i)

for i in range(len(s1)):
    if s1[i] == 'o':
        print('The o found at index', i)


print(ord('a'))
print(chr(97))
print("hello")
print(pow(2,38))

s3= '''g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. 
bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. 
sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.'''

str1 = ''
for i in s3:
    if i.isalpha():
        if i == 'y':
            str1 += chr(97)
        elif i == 'z':
            str1 += chr(98)
        else:
            value = (ord(i) + 2)
            str1 += chr(value)
    else:
        str1 += i
print(str1)

s3 = 'map'
str1 = ''
for i in s3:
    if i.isalpha():
        if i == 'y':
            str1 += chr(97)
        elif i == 'z':
            str1 += chr(98)
        else:
            value = (ord(i) + 2)
            str1 += chr(value)
    else:
        str1 += i
print(str1)

l = ['lion', 'tiger', ['foo', 'bar']]
l2 = l[:]

s = 'hello world'
print(s)