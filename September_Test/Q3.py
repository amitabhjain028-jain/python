num=int(input("Enter a number: "))

temp=num
length=0
sum=0
largest_digit=0
smallest_digit=9
reverse=0

while num!=0:
    r=num%10
    sum=sum+r
    reverse=reverse*10+r
    if largest_digit<r:
        largest_digit=r
    if smallest_digit>r:
        smallest_digit=r
    length+=1
    num=num//10

print(f"\nSum of digits: {sum}")
print(f"Number of digits: {length}")
print(f"Largest digit: {largest_digit}")
print(f"Smallest digit: {smallest_digit}")
if temp==reverse:
    print("Palindrome: Yes")
else:
    print("Palindrome: No")