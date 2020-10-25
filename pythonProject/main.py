names = ["Bianca", "Neil", "YourMa"]

#names.append("Ciaran")

#print(names[:])

#for name in names:
#    print(name)
#    print("\n")
#for i in range(10):
#    print(i, end="*")

#my_numbers = [10, 20, 30, 40]
#for i in range(len(my_numbers)):
#    print(my_numbers[i], end=" ")

#my_sum = 0
#for i in range(1,11):
#    my_sum +=i

#print("Sum of first 10 natural numbers : ", my_sum)

#for i in range(2,26,2):
#    print(i, end=" ")

#price = input("how much does it cost? ")

#if float(price) >= 1.00:    #casting string to a float...
#    tax = 0.07
#    print(tax)
#else:
#    tax = 0
#    print(tax)

#if price.isdigit():
#    print("yayyy")
#else:
#    print("nayyy")
#my_numbers = [10, 20, 30, 40]
#index = 0
#while index < len(my_numbers):
#    print(my_numbers[index])
#    index += 1
fruits = ("apple", "banana", "pear")
for index, fruit in enumerate(fruits):
    print("index is %d and value is %s"% (index, fruit))
