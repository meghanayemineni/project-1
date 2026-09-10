num1=int(input())
num2=int(input())
op=input(" Enter operator +, -, *, /, //, **, % :") 
if op=="+":
    result=num1+num2
    print(result) 
elif op=="-":
    result=num1-num2
    print(result)
elif op=="*":
    result=num1*num2 
    print(result)  
elif op=="/":
    result=num1/num2
    print(result)
elif op=="%":
    result=num1%num2 
    print(result)
elif op=="//":
    result=num1//num2
    print(result)
elif op=="**":
    result=num1**num2 
    print(result) 
else:
    print("invalid number") 