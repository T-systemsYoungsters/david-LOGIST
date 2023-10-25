#David Vilhena Klein
#05.10.2023
# print a box out of o's in command line

n=int(input("How big should the box be? n = "))
for i in range(n):
    print(end="oo")
print()
for i in range(n-2): #hab hier einfach -1 gemacht^^
    print("o", end="")
    for j in range(n-1):
        print("  ", end="")
    print("o")
for i in range(n):
    print(end="oo")