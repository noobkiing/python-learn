n= int(input("Number: "))        # input fuction does not know that you are typing nuber, it consider it as string;
if n > 0:                        #so int function cinverts the str to int
    print("n is positive")
elif n < 0:
    print("n is negative")
else:
    print("n is zero")