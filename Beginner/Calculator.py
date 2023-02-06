def Add(n1 , n2 ):
    return n1 + n2 
def subtract(n1, n2 ) : 
    return n1-n2
def multiply(n1 , n2 ):
    return n1*n2
def divide (n1,n2):
    return n1/n2 

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
ans = input ("if you want to continue press Y ")
Contiue_prog = True
while Contiue_prog :
    if(ans=="y"):
     
        a=int(input("enter the first number "))
        b=int(input("enter the second number "))
        op = input("which operation you want to do")

        if (ans== "y"):
         function = operation[op]
         print(f"THE ANSWER IS = {function(a,b)}")
    else :
        Continue_prog = False
        print("END")
        Continue_prog= False 
        break

   
