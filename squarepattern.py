'''

***********
***** *****
****   ****
***     ***
**       **
*         *
**       **
***     ***
****   ****
***** *****
***********

'''

num= int(input("Enter the number : "))
print("-"*((num*2)+1))
for i in range(-num, num+1, +1):
   if i!=0 and i!=1:
    print("$"*abs(i), end="")
    print(" "*(2*(num-abs(i))+1), end="")
    print("$"*abs(i), end="")
    print("\r")
print("-"*((num*2)+1))
