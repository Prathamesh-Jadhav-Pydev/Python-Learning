a="Hello"
b=30
c=40.678
d=True
e=None
#Print variable
print(a)
print(b)
print(c)
print(d)
print(e)
#check variable type
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))

#Arithmatic Operator
a=int(input("Enter Number A"))
b=int(input("Enter Number B"))
print("Addition",a+b)
print("Subtraction",a-b)
print("Multiplication",a*b)
print("Division",a/b)
print("Remainder",a%b)

#assignment operator
c=25
c+=10
print(c)
c-=10
print(c)
c*=10
print(c)
c/=10
print(c)

#Compariosn Operator
d=20
e=45
print("D is greater than E",d>e)
print("D is less than E",d<e)
print("D is greater than equal to E",d>=e)
print("D is less than equal to E",d<=e)
print("D is exactly equal to E",d==e)
print("D is not equal to E",d!=e)


#Average of two number
print("Enter first number")
Num_1=int(input())
print("Enter first number")
Num_2=int(input())
avg=(Num_1+Num_2)/2
print("Average of two number is ",avg)

#Square of numbers
print("Enter number to calculate square")
Num_1=int(input())
Squr=Num_1*Num_1
print("Square of number is",Squr)

#Typecasting 
num_1=input("Enter a Number")
print(num_1)#number is in the form of string
print(type(num_1))

num_1=int(num_1)#string to int conevrt
print(num_1)
print(type(num_1))

num_1=float(num_1)#num to float convert
print(num_1)
print(type(num_1))


#Logical operators
bool1=True
bool2=False
print("AND Operator",bool1 and bool2)
print("OR Operator",bool1 or bool2)
print("NOT Operator",not bool2)
