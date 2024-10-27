s1 ='mysirg education services'
print(len(s1))
print(s1.index('i'))
print(s1.index('sir'))
print(s1.count('i'),s1.count(' '))
print(s1.startswith('my'),s1.endswith('services'))
s2,s3='a123','123'
print(s2.isdigit(),s3.isdigit())
print(s1.islower(),s1.isupper())
print(s1.lower(),s1.upper())
s4=s1.replace('i','I',s1.count('i'))
print(s1)
print(s4)

