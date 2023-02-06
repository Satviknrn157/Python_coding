num_cans=1
def paintcans(height,width):
	num_cans = height*width
	num_cans= num_cans/5
	print(f"the number of cans = {num_cans}")

h=int(input("enter the height"))
w=int(input("enter the width"))
paintcans(h,w)