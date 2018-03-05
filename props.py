from twistedints import TwistedInt

# Used to test what kind of values the mathematical functions give

for x in range(1, 101):
    print(TwistedInt.isAddCommutative(x))

print("\n")
for x in range(1, 101):
    print(TwistedInt.isMulCommutative(x))

print("\n")
for x in range(1, 101):
    print(TwistedInt.isAddAssociative(x))

print("\n")
for x in range(1, 101):
    print(TwistedInt.isMulAssociative(x))

print("\n")
for x in range(1, 101):
    print(TwistedInt.isDistributive(x))