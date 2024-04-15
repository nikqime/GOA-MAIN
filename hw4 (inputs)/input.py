pepsi = int(input("Please enter product price for Pepsi: "))
fanta = int(input("Please enter product price for Fanta: "))
fusetea = int(input("Please enter product price for Fuse Tea: "))

if pepsi >= 600 and pepsi <= 1000:
    print("I'm declining Pepsi because of its high price")
elif pepsi >= 1 and pepsi <= 600:
    print("Deal for Pepsi!")

if fanta >= 600 and fanta <= 1000:
    print("I'm declining Fanta because of its high price")
elif fanta >= 1 and fanta <= 600:
    print("Deal for Fanta!")

if fusetea >= 600 and fusetea <= 1000:
    print("I'm declining Fuse Tea because of its high price")
elif fusetea >= 1 and fusetea <= 600:
    print("Deal for Fuse Tea!")
