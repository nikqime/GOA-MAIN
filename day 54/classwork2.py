first=int(input("Enter First here :"))
second=int(input("Enter second here :"))
third=int(input("Enter third here :"))

if first+second>third:
    print("yes")
elif first+second<third:
    print("no")
elif second+third<first:
    print("no")
elif second+third>first:
    print("yes")
elif third+first>second:
    print("yes")
elif third+first<second:
    print("no")