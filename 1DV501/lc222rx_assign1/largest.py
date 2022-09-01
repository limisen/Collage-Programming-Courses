from re import A


print("Please provide three integers A, B, C.")
A = int(input("Enter A: "))
B = int(input("Enter B: "))
C = int(input("Enter C: "))

if A > B and A > C:
    print("The largest number is: " + str(A))
elif B > A and B > C:
    print("The largest number is: " + str(B))
elif C > A and C > B:
    print("The largest number is: " + str(B))