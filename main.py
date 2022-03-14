first=int(input("enter the first number : "))
second=int(input("enter second number : "))
op=input("enter operator : ")
if op=='+':
    print(first+second)
elif op=='-':
    print(first-second)
elif op=='*':
    print(first*second)
elif op=='/':
     print(first//second)
else:
     print("invalid operator")
