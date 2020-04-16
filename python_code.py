num = int(input("enter number:"))
reverse = num
a=0
while reverse!= 0:
    a = a*10
    a = a+(reverse%10)
    reverse = int(reverse/10)
if a == num:
    print("yes")
else:
    print("no")

