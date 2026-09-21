def cal(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    elif op == '/':
        if b == 0:
            return "can not divide"
        else:
            return a / b

print("\n ... Calculator ...")
print(" + for Add \n - for Subtraction \n * for multiply \n / for division \n e for exit the calculator")

while True:
    op = input("Enter operation: ")
    if op=='e':
            print("calculator closed")
            break
    a=int(input("enter a="))
    b=int(input("enter b="))
    
    result=cal(a,b,op)
    print("Result=",result)