# calculating u mentioned in the formula 
def u_cal(u, n): 
	temp = u; 
	for i in range(1, n): 
		temp = temp * (u - i); 
	return temp; 

# function for factorial
def fact(n): 
	f = 1; 
	for i in range(2, n + 1): 
		f *= i; 
	return f; 


#------------------------------------Main Code----------------------------------------#

print("-----------------------------Newton Forward and Backward Interpolation----------------------\n")
# Number of values given
n = int(input("Enter the no of value=")); 
print("Enter the value of x like 20 30 40..... space-seperated")
x = list(map(int,input().split())) 
	
# y[][] is used for difference table 
# with y[][0] used for input 
y = [[0 for i in range(n)] 
		for j in range(n)]; 

print("\n\nEnter the corresponding value of X")

for i in range(0,n):
    print("\nEnter value for x=",x[i])
    y[i][0]=float(input())


value =float(input("Enter the value of X need to be find=" ))

# Calculating the forward difference 
# table 

print("\n\n\n------------------------------Difference Table------------------------------\n")
for i in range(1, n):
	for j in range(n - i): 
		y[j][i] = y[j + 1][i - 1] - y[j][i - 1]

# Displaying the forward difference table 
for i in range(n): 
    print(x[i], end = "\t"); 
    for j in range(n - i): 
        print(y[i][j], end = "\t")
    print("")
  
print("\n")
# initializing u and sum 
sum = y[0][0]; 
u = (value - x[0]) / (x[1] - x[0]); 
for i in range(1,n): 
    sum = sum + (u_cal(u, i) * y[0][i]) / fact(i); 
  
print("\nValue at", value,  
      "is", round(sum, 7)); 

print("\n\n---------------------------------end--------------------------------")