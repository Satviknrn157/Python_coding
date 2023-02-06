ent = 1 

def function():
    ent = 3 #this is ent out side the function , it is another ent (local) that is printing
    want = 3
    print('in the funtion ')
    return ent

def function2 ():
    #ent = ent +1 #you cannot do this 
    print(ent)
# you cannot modify in function if you want to you have to put GLOBAL infront of variable
def function2 ():
    global ent
    ent = ent +1 #you cannot do this 
    print(ent)

print(function())
function2()
print(ent)
#print(want)  here you cannot print this due want being a local variable

# here the ent is not printing what we changed in the function
#inside the function is called "LOCAL VARIABLE" 

#so ent is global variable 
def one():
    one = 1
   
  #  print(two)  # here two is local variable but one is READABLE to two
    def two():
     two = 2 
     print(one)
    two()


one()

def create_enemy():
    enimies = 32

    if 3>2:
         print(enimies) #here if is under the function
         enimies =33
         enimies2=34

    print(enimies2) #

enimies2 = 35
print("outside is 35")
print(enimies2)
create_enemy()

# You can access enimeies 2 outside the function also AS IT IS IN THE LOOPS
# for if , for , while function scoping is global only
PI = 3.1432 
pi =3.1432
#UPPERCASE PI - is constant . you cannot change it 

