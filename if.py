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

#Homework
'''principal= int(input("Enter a principal: "))
rate= int(input("Enter a rate: "))
time= int(input("Enter a time: "))
a= principal*time*rate/100
print(a)'''


#calculation
x= int(input("Enter a Number:  "))
y= int(input("Enter a Number:  "))
print("Enter a character to perform")
ch= input("Enter a character to perform a,b,c,d:  ")
result= 0
if ch=='a':
    result= x+y;
    print(result)
elif ch=='b':
    result=x-y;
    print(result)
elif ch=='c':
    result=x*y;
    print(result)
else:
    result=x/y;
    print(result)