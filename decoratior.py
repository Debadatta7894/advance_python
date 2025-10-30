def decore4(cal):
    def all(a,b):
        add = a + b
        sub = a - b
        mul = a * b
        div = a / b
        return add,sub,mul,div
    return all

def decore3(cal):
    def division(a,b):
        res = a / b
        return res,cal(a,b)
    return division

def decore2(cal):
    def substrc(a,b):
        res = a - b
        return res,cal(a,b)
    return substrc

def decore(cal):
    def mul(a,b):
        res = a * b
        return res,cal(a,b)
    return mul  

  
@decore4
@decore3
@decore2
@decore
def cal(a,b):
    add = a + b
    return add
num1 = int(input("Enter a number : "))
num2 = int(input("Enter a number : "))
print(cal(num1,num2))