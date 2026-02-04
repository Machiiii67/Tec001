#1
num = 1
while num <= 1000:
    if num % 3 == 0:
        print (num)
    num += 1
#2 convert
while True:
    inch = float(input("Enter inch : "))
    if inch < 0:
        break
    else:
        cm = inch * 2.54
    print("cm:", cm)
#3
largest = None
smallest = None
while True:
    s = input("Enter a whole number or empty string to quit: ")
    if s == "":
        break
    try:
        num = float(s)
    except:
        print ("Invalid input, please enter a number.")
        continue
    if largest is None or num > largest:
        largest = num
    if smallest is None or num < smallest:
        smallest = num
print ("largest", largest)
print ("smallest", smallest)
#4
count = 0
correct_username = "python"
correct_password = "rules"
while True:
    u = input("Enter username: ")
    p = input("Enter password: ")
    if u == correct_username and p == correct_password:
        print("Welcome")
        break
    else:
        print ("wrong username or password, try again")
        count +=1
        if count == 5:
            print ("Access denied")
            break

#5
w = input("enter string:")
def middle(w):
    m = len(w)
    if m % 2 == 1:
        return w[m//2]
    else:
        return w[m//2 - 1] + w[m//2]
#6
s = input ("Enter a sentence: ")
words = s.split()
finish = ""
for n in words:
    finish = finish + n[0].upper()
print (finish)
#6
def acronym(s):
    words = s.split()
    result = ""
    for w in words:
        result += w[0].upper()
    return result
print(acronym("unidentified foreign object"))