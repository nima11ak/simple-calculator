a = float(input("عدد اول :"))
b = input("{+,- , *,/} :")
c = float(input("عدد دو : "))


if  b == "+":
    print("نتيجه:",a ,b, c,'=', a+c)


elif b == "-":
     result = a - c
     print("نتيجه:", result)
    
 
elif  b == "*":
    result = a * c
    print("نتيجه:", result)
    

elif  b == "/":
    result = a / c
    print(result,"نتيجه:")
    

else:
    print("warng","(اشتباه)")
    
