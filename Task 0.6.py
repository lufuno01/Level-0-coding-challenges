
def finding_the_largest_number(number1,number2,number3):
 if (number1 > number2) and (number1 > number3):
      number = number1
     
 elif (number2 > number3) and (number2 > number1):
      number = number2
    
 else:
     number = number3
     
 print("The highest number is ",number)   
finding_the_largest_number() 
