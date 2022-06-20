import random
import math

smaller = int(input("Enter a smaller number: "))
larger = int(input("Enter a larger number: "))

count = 0

print()
while True:
    count += 1
    myNumber = (smaller + larger) // 2
    print('%d %d' % (smaller, larger))
    print('Number is: %d' % myNumber)
    choice = input('Enter =, <, or >: ')
    if choice == '=':
        print("Done in %d tries" % count)
        break
    elif smaller == larger:
        print("Out of guesses!")
        break
    elif choice == '<':
        larger = myNumber - 1
    else:
        smaller = myNumber + 1  


            
