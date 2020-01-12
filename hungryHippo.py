# The hippo eats the largest number

def hungry_hippo(num1, num2, num3):
     
    if num1 >= num2 and num1 >= num3:
        return num1
    if num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3
print(hungry_hippo(8851, 999999, 1000))