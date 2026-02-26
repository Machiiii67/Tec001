#1
number = []
while True:
    enter_number = (input("Enter a number: "))
    if enter_number == "":
        break
    number.append(int(enter_number))
sorted_number = sorted(number, reverse=True)[:5]
print(sorted_number)
#2
def kind_of_number(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n > 2 and n % 2 ==0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                return False
    return True
try:
    number = int(input("Enter a number: "))
    if kind_of_number(number):
        print(f"{number} is a prime number.")
    else:
        print(f"{number} is not a prime number.")
except ValueError:
    print("That is not a valid integer.")
#3
cities = []
for i in range(5):
    city = input(f"City {i + 1}: ")
    cities.append(city)
print("\nCities you entered:")
for city in cities:
    print(city)
#4
def sum_1(n):
    total = 0
    for num in n:
        total += num
    return total
numbers = []
while True:
    number = input("Enter a number (blank to stop): ")
    if number == "":
        break
    try:
        numbers.append(int(number))
    except ValueError:
        print("Please enter a valid integer.")
result = sum_1(numbers)
print("The sum is:", result)
#5
def remove_odd_numbers(numbers):
    even_numbers = []
    for number in numbers:
        if number % 2 == 0:
            even_numbers.append(number)
    return even_numbers
def main():
    original_list = [1, 2, 3, 4, 5, 6, 7, 8]
    filtered_list = remove_odd_numbers(original_list)
    print("Original list:", original_list)
    print("List without odd numbers:", filtered_list)
main()