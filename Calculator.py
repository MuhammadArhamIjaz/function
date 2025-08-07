def add(p,q):
    return p+q
def subtract(p,q):
    return p-q
def multiplication(p,q):
    return p*q
def division(p,q):
    return p/q
print("Pick an operation")
print("A.Addition")
print("B.Subtraction")
print("C.Multiplication")
print("D.Division")
choice=(input("Enter the option A,B,C,D"))
num1=int(input("Enter number 1"))
num2=int(input("Enter number 2"))      
if choice=='A':
    print( num1 ,"+" ,num2,"=",add(num1,num2))
elif choice=='B':
    print( num1 ,"-" ,num2,"=",subtract(num1,num2))
elif choice=='C':
    print( num1 ,"*" ,num2,"=",multiplication(num1,num2))
elif choice=='D':
    print( num1 ,"/", num2,"=",division(num1,num2))
else:
    print("Invalid input")