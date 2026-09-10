num1=int(input(""))
num2=int(input())

op=input(" Enter operator +, -, *, /, //, **, % : ") 

if op=="+":
    result=num1+num2
    print(f" result: {result}")

elif op=="-":
    result=num1-num2
    print(f" result: {result}")

elif op=="*":
    result=num1*num2 
    print(f" result: {result}")

elif op=="/":
    result=num1/num2
    print(f" result: {result}")

elif op=="%":
    result=num1%num2 
    print(f" result: {result}")

elif op=="//":
    result=num1//num2
    print(f" result: {result}")

elif op=="**":
    result=num1**num2 
    print(f" result: {result}") 