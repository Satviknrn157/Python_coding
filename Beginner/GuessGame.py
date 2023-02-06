import random
num = random.randrange(1,100) 

diff = input("Choose the difficulty easy or hard") 

def guess_function(num , att):
    
    at = att
    for i in range(att):
        guessed_num = int(input("Make a guess"))
        if guessed_num == num :
            print("Correct answer")
            break
        elif guessed_num>num:
            print("too high try again")
            at = at- 1
            print(f"you have {at} attempts remaining")
        elif guessed_num<num:
            print("too Low try again")
            at = at- 1
            print(f"you have {at} attempts remaining")
        if(at==0):
            print(f"the correct answer is = {num}")
    

if diff == "easy":
   
    attempts = 10
    print(f"You have {attempts}")
    guess_function(num , attempts)
elif diff == "hard" :
    attempts=5
    print(f"You have {attempts}")
    guess_function(num , attempts)
else :
    print("OOPS try again")

