height = int(input("Enter the height of the pyramid: "))
alpha=["A","B","C","D","E","F","G","H","I","J"] #max 10
for i in range(0,height):
    for j in range(0,height):
       print(alpha[j],end=" ")
        
    print()