#1
numbers = []
while True:
    user_input = input("Enter a number (empty to quit): ")

    if user_input == "":
        break
    number = float(user_input)
    numbers.append(number)
numbers.sort(reverse=True)
print("The five greatest numbers are:")
for number in numbers[:5]:
    print(number)
#2
seasons = ("winter", "spring", "summer", "autumn")
month = int(input("Enter the number of a month (1-12): "))
if month >= 1 and month <= 12:
    if month == 12 or month == 1 or month == 2:
        season = seasons[0]
    elif month >= 3 and month <= 5:
        season = seasons[1]
    elif month >= 6 and month <= 8:
        season = seasons[2]
    else:
        season = seasons[3]
    print("Season is", season)
else:
    print("Invalid month number")
#3
names = set()
while True:
    name = input("Enter a name (empty to quit): ")
    if name == "":
        break
    if name in names:
        print("Existing name")
    else:
        print("New name")
        names.add(name)
print("\nNames:")
for name in names:
    print(name)
#4
def word_frequency(text):
    words = text.lower().split()
    counts = {}
    for word in words:
        counts[word] = counts.get(word, 0) + 1
    sorted_words = sorted(counts.items(), key=lambda x: x[1], reverse=True)
    top5 = sorted_words[:5]
    total_words = len(words)
    top5_total = sum(count for word, count in top5)
    proportion = (top5_total / total_words) * 100
    print("Top 5:", dict(top5))
    print("Total number of words:", total_words)
    print("Proportion of 5 most common words:", round(proportion, 2), "%")

text = input("Enter text: ")
word_frequency(text)
#5
def remove_odd_numbers(numbers):
    even_numbers = []
    for number in numbers:
        if number % 2 == 0:
            even_numbers.append(number)

    return even_numbers
original_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
cut_down_list = remove_odd_numbers(original_list)
print("Original list:", original_list)
print("Cut-down list:", cut_down_list)