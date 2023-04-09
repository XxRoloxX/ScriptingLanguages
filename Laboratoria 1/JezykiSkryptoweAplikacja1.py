#Example script


#print("Hello world")

def triangleField(height, side):
    if(height.isnumeric() and side.isnumeric()):
        return int(height)*int(side)/2
    else:
        return 0

userHeight = input("Enter triange height: ")
userSide = input("Enter triange side length: ")
print(f"Triangle field is: {triangleField(userHeight, userSide)}")


#print(triangleField(userHeight, userSide))

