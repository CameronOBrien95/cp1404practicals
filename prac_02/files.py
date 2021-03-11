# #1.
user_name = input("Enter your name: ")
name_file = open("name.txt", 'w')
name_file.write(user_name)
name_file.close()

# #2.
name_file = open("name.txt", 'r')
user_name = name_file.read()
print("your name is {}".format(user_name))
name_file.close()

#3.
number_file = open("numbers.txt", 'r')
numbers = number_file.readlines()
number_one = int(numbers[0])
number_two = int(numbers[1])
number_file.close()
total = number_one + number_two
print(total)

#4.
total =0
number_file = open("numbers.txt", 'r')
numbers = number_file.readlines()
number_file.close()
for line in numbers:
    total += int(line)
print(total)





