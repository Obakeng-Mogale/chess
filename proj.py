for i in range(5):
    for j in range(5):
        if ((i==2 or j ==2)or(i==1 or i==3)and(j==1 or j==3)):
            print("* ",end="")
        else:
            print("  ",end="")

    print('')
        