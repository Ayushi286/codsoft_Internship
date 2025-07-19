def calculator(a,b,choice):
  if(choice=="1"):
    print("Result:",a+b)
  elif(choice=="2"):
     print("Result:",a-b)
  elif(choice=="3"):
    print("Result:",a*b)
  elif(choice=="4"):
   if(b!=0):
      print("Result:",a/b)
   else:
    print("Error,cannot divide by Zero")
  elif(choice=="5"):
    print("Result:",a%b)  
  else:
    print("Invalid choice")

num1=float(input("Enter first number"))
num2=float(input("Enter second number"))

print("\nChoose an operation:")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")
print("5. Remainder(%)")

choice = input("Enter your choice (1/2/3/4/5): ")
calculator(num1, num2, choice)

  
