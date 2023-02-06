def Add(n1 , n2 ):
    return n1 + n2 
def subtract(n1, n2 ) : 
    return n1-n2
def multiply(n1 , n2 ):
    return n1*n2
def divide (n1,n2):
    return n1/n2 

a=int(input("enter the first number "))
b=int(input("enter the second number "))

"""
op=input("what operation you want to do")
if(op=="*"):
    multiply(a,b)
elif(op=="-"):
    subtract(a,b)
elif(op=="+"):
    Add(a,b)
else:
    divide(a,b)
    """

#dictionary
operation={
    "*": multiply,
    "+":Add,
    "/":divide
    
}
op = input("which operation you want to do")

function = operation[op]
print(function(a,b))
