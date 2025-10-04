#print("square using star")
#for i in range(6):
    #for j in range(6):
        #print("*", end=" ")
    #print()

print("star pattern")
n=int(input("Enter the limit: "))
for i in range(1,n+1):
    for j in range(i):
        print("*", end=" ")
    print()

