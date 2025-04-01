# functions for operations
def add(a):
    sum = 0
    for i in a:
        sum += i
    return sum
def sub(a):
    diff = a[0]-a[1]
    return diff
def mult(a):
    prod = 1
    for i in a:
        prod *= i
    return prod
def div(a):
    quot = a[0]/a[1]
    return quot
def mod(a):
    mod = a[0] % a[1]
    return mod
def floor(a):
    quot2 = a[0]//a[1]
    return quot2

def start():
    #Hello welcome to the amazing calculator!
    #Input any numbers along with operations (+,-,/,*,%,//)
    calc()
def calc():
    while True:
        inputs = []
        user_input = input("Input your calculation")
        inputs.append[user_input]
        for i in inputs:
            string += i
            print(string)
        if user_input == "=":
            solution(inputs)
            break
def solution(inputs):
    num = [1,2,3,4,5,6,7,8,9,0]
    operator = ['+','-','/','*','%','//']
    while True:
        index = set(operator) & set(inputs)
        if index == []:
            error()
            break
        for i in index:
            if index[i-1] in num and index[i+1] in num:
                # operation
                pass
            else:
                error()
                break

def error():
    print("error")
    calc()





