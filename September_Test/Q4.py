numb1=int(input("Enter start: "))
numb2=int(input("Enter end: "))

counts=0
print("Prime numbers:")

for i in range (numb1+1,numb2):
    n=2
    while n<=i//2:
        if i%n==0:
            break
        n=n+1
    if n>i//2 and i>1:
        print(i,end=" ")
        counts+=1
    
print(f"\nTotal prime numbers: {counts}")