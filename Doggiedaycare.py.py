# The following is a list of dogs currently at Doggie Daycare
dogs = ['Skye','Mabel','Lassie','Buttercup']

# Do not change any of the code above this line!

# Write a line of below to print out the list of dogs currently at daycare
print('-'*65)
print()
print()
print('These dogs are currently at the daycare!: ' + str(dogs))




# The following dogs have just arrived to daycare, programatically add each of them to the list of dogs at daycare
# Widget, Balto, Chloe
# When you are done adding all three dogs, print out the list of dogs currently at daycare

dogs.append('Widget')
dogs.append('Balto')
dogs.append('Chloe')
print('-'*15)
print()
print()
print('Three new dogs have just arrived at the daycare! These dogs are currently at the daycare!: ' + str(dogs))


# Sort the dogs alphabetically
# When you are done print out the list of dogs currently at daycare

dogs.sort()
print('-'*15)
print()
print()
print('These dogs are currently at the daycare, in alphabetical order!: ' + str(dogs))


# Programatcially print out a list of the first three dogs.

print('-'*15)
print()
print()
print('These are the first three dogs currently at the daycare!: ' + str(dogs[0:3]))



# Mabel and Buttercup have been picked up by there owners, so they are no longer at doggie daycare
# Write some lines of code removing both from the list
# When you are done print out the list of dogs currently at daycare
print('-'*15)
print()
print()
dogs.remove('Mabel')
dogs.remove('Buttercup')

print('Two dogs have just been picked up by their owners! These dogs are currently at the daycare!: ' + str(dogs))
print('-'*65)

