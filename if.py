#learning python
'''age= int(input("Enter your age:"))
if age > 18:
print("You are above 18")
elif age == 18:
    print("You are equal to 18")
else:
    print("You are below 18")'''
#single line:
#grade= int(input("Enter your marks: "))
#result= "pass" if grade > 40 else "fail"
#print(result)

#nested loop
'''grade =int(input("Enter your marks: "))
if grade > 40:
    if grade >= 60:
        if grade < 80:
            print("First Division")
    elif grade >= 80 and grade < 90:
        print("Distinction")
    else:
        print("Second Division")
else:
    print("Fail")'''

'''#Homework
principal= int(input("Enter a principal: "))
rate= int(input("Enter a rate: "))
time= int(input("Enter a time: "))
SI= principal*time*rate/100
print("SI", SI)'''


'''#calculation
x= int(input("Enter a Number:  "))
y= int(input("Enter a Number:  "))
ch= input("Enter a character to perform a,b,c,d:  ")
if ch=='a':
    a= x+y
    print(a)
elif ch=='b':
    b=x-y
    print(b)
elif ch=='c':
    c=x*y
    print(c)
else:
    d=x/y
    print(d)'''


#String
'''name="Razesh Baziko"
a=name.split()
print(a)
name="          Razesh Baziko     "
print(name.strip())
print(name.upper())
print(name.replace("R","r"))'''

#split()
'''name=input("Enter your full name: ")
x=name.split()
print(x)'''


#.indigit string
'''text=input("Enter a text:  ")
x=text.isdigit()
print(x,text)'''


#capitalize
'''name=input("Enter a full name:  ")
x=name.title()
print(x) '''


#vowel character
name=input("Enter a name: ")
Vowel="aeiou"
for word in name:
    if word in Vowel:
        print("Vowel :",word)
    