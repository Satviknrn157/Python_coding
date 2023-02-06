p=int(input("enter the prime number"))

def check_prime(num):
  check = True
  for i in range(2, p):
    if(num%i==0):
      check = False
      print("it is not a prime number")

      break
  if(check ==True ):
        print("it is a prime number")

check_prime(p)