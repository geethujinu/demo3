
rows = int(input("Enter number of rows: "))

for p in range(rows):
    for j in range(p+1):
        print("* ", end="")
    print("\n")
