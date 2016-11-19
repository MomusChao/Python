#25 str.replace()

#str.replace(old,new[,count])
string = 'I have an apple, I have a pen.'

#replace 'have' with 'had'
print(string.replace('have','had'))

#original variable didn't change. It's Call By Value
print(string)

#replace first 'have' with 'had'
print(string.replace('have','had',1))
