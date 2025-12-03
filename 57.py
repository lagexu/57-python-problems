height = int(input("Enter Your Height: "))
alpha=["A","B","C","D","E","F","G","H","I","J"] #max 10
for i in range(height,0,-1):
    for j in range(i,0,-1):
        print(alpha[j-1],end=' ')
    print()