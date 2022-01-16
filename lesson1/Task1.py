#1
num_1 = 10
num_2 = 15
amount = num_1 + num_2
print(amount)

#2
name = "Alex"
surname = "Ivanov"
print("You are welcome, " + name, surname)

#3
user_age = int(input("Please, enter your age: "))
if user_age >= 18:
    print("You can enter")
else:
    print("Wait for some time :)")

#4
city = input("Enter your city: ")
address = input("Enter your street: ")
address_1 = int(input("Enter your building's number: "))
message = "Please, check data you entered. You live in %s city, on %s Street, you house number is %d." %(city, address, address_1)
print(message)