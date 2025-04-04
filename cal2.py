# functions for operations
def add(a):
    sum = 0
    for i in a:
        sum += i
    return "solution" + sum
def sub(a):
    diff = a[0]-a[1]
    return "solution" + diff
def mult(a):
    prod = 1
    for i in a:
        prod *= i
    return "solution" + prod
def div(a):
    quot = a[0]/a[1]
    return "solution" + quot
def mod(a):
    mod = a[0] % a[1]
    return "solution" + mod
def floor(a):
    quot2 = a[0]//a[1]
    return "solution" + quot2

def start():
    print("Hello welcome to the amazing calculator!")
    print("Input any numbers along with operations (+,-,/,*,%,//)")
    calc()
def calc():
    string = ""
    inputs = []
    while True:
        
        
        user_input = input("Input your calculation: ")
        inputs.append(user_input)  
        string += user_input
        print(string)
        if user_input == "=":
            solution(inputs)
            break
def solution(inputs):
    
    num = ['1','2','3','4','5','6','7','8','9','0']
    operator = ['+','-','/','*','%','//']
    ans = 0
    index = -1
    while True:    
        for item in inputs:
            if item in operator:
                index = inputs.index(item)
        if index == -1:
            error()
            break 
        
        if inputs[index-1] in num and inputs[index+1] in num:
            insert = [int(inputs[index-1]),int(inputs[index+1])]
            if inputs[index] == "+":
                print(add(insert))
                calc()
            if inputs[index] == "-":
                print(sub(insert))
                calc()
            if inputs[index] == "*":
                print(mult(insert))
                calc()
            if inputs[index] == "/":
                print(div(insert))
                calc()
            if inputs[index] == "%":
                print(mod(insert))
                calc()
            if inputs[index] == "//":
                print(floor(insert))
                calc()
        else:
            error()
            break

def error():
    print("error") 
    calc()

start()




