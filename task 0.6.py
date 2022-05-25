
def finding_the_largest_number(number1,number2,number3):
 if (number1 > number2) and (number1 > number3):
      number = number1
      return number
 elif (number2 > number3) and (number2 > number1):
      number = number2
      return number
 else:
     number = number3
     
     return number
  
print(finding_the_largest_number(22,5,27)) 
