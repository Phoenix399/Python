def ONCubeTime(n):
    iteration = 0
    for i in range(0, n):        # 1st loop
        for j in range(0, n):    # 2nd loop
            for k in range(0, n):  # 3rd loop
                print("*", end=" ")
                iteration += 1
            print("")            # New line after inner loop
        print("")                # Space between blocks

    print("\nWhen n is", n, "iteration =", iteration, "\n")


ONCubeTime(5)
ONCubeTime(4)
ONCubeTime(3)

print("\nWith every 'n' the time taken equals n^3")
print("O(n^3)")
