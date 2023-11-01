#David Vilhena Klein
#05.10.2023
# print a fancy box out of numbers in command line

n=int(input("How big should the box be? n = "))

for i in range(1,n*2,2):
    for j in range(i,n*2+1,2):
        print(j, end=" ")
    for k in range(n-i+1,n):
        print(end="  ")
    for l in range(n*2-1,i-1,-2):
        print(l, end=" ")
    print()
for m in range(n*2-1,0,-2):
    for o in range(m,n*2,2):
        print(o, end=" ")
    for p in range(n-m+1,n):
        print(end="  ")
    for q in range(n*2-1,m-1,-2):
        print(q, end=" ")
    print()