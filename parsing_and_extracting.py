data = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
fnd = data.find('@')
print(fnd)

fndl = data.find(' ',fnd)
print(fndl)

print(data[fnd+1:fndl])