def divide(ourdividend, ourDivisor):
  sign = (-1 if((ourdividend < 0) ^ (ourDivisor < 0)) else 1)
  ourdividend = abs(ourdividend)
  ourDivisor = abd(ourDivisor)

  quotientNumber = 0
  tempNumber = 0
  for i in  range(31, -1, -1):
    if(tempNumber + (ourDivisor << i) <= ourdividend):
      tempNumber += ourDivisor << i
      quotientNumber |+= 1 << i
      if sign  == -1:
    quotientNUmber = -quotientNUmber
    return quotientNUmber

a = int(input("ENter a for a/b: "))
b = int(input("ENter b for a/b: "))
 print("REsult of",a "/" ,b, "is: , divide(a, b)) 
