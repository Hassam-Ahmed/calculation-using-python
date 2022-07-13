#first functional defined program in python...

#def max_num(num1, num2, num3):
 #   if num1 >=  num2 and num1 >= num3:
  #      return num1
   # elif num2 >= num3 and num2 >= num3:
    #    return num2
    #else:
     #   return num3
#
#print(max_num(33, 23, 55))

x = float(input("Enter first number: "))
op = input("Enter operator: ")
y = float(input("Enter second NUmber: "))

if op == "+":
    print("The Addition of " +str(x)+ " and " +str(y)+ " is = ",x + y)
elif op == "-":
    print("The subtraction of " +str(x)+ " and " +str(y)+ " is = ",x - y)
elif op == "*":
    print("The Multiplication of " +str(x)+ " and " +str(y)+ " is = ",x * y)
elif op == "/":
    print("The Division of " +str(x)+ " and " +str(y)+ " is = ", x / y)
else :
    print("Enter a valid Number")