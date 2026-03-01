print("******TEMPERATURE CONVERTER******")
choice1="convert fahrenheit to celsius"
choice2="convert celsius to fahrenheit"
choice=int(input("enter your choice:"))
x=float(input("enter value of temperature:"))
if (choice==1):
    print("converting fahrenheit to celsius")
    print("temp=",(x-32)*(5/9))
elif (choice==2):
    print("converting celsius to fahrenheit")
    print("temp=",(x*9/5)+32)
else:
    print("invalid choice")