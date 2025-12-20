#program to check if the nth bit is set or  not set

def setOrNot(number, n):

    #MAke a mask variable by left shifting 1(K-1)times and check if (n AND mask)equals 1 or 0
          if number & (1 <<(n - 1)):
              print( "\nSET")
          else:
               print( "\nNOT SET")

number = int(input("Enter number : "))
n = int(input("Enter bit number : "))
setOrNot(number, n)
