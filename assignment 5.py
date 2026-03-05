#1
import re
code = input("Enter course code: ")
pattern = r'^[A-Z]{2,3}[0-9]{3}$'
if re.match(pattern, code):
    print("True")
else:
    print("False")
#2
import re
color = input("Enter hex color: ")
pattern = r'^#[0-9A-Fa-f]{6}$'
if re.match(pattern, color):
    print("Valid hex color")
else:
    print("Invalid hex color")
#3
import re
text = input("Enter a paragraph: ")
numbers = re.findall(r'\d+', text)
total = sum(int(n) for n in numbers)
print("", total)
#4
import re
def redact_phones(s):
    phone_pattern = r'(\+84\d{8,12}|\b\d{10}\b)'
    return re.sub(phone_pattern, "[REDACTED]", s)
user_text = input("Enter text: ")
print(redact_phones(user_text))
#5
import random
N = int(input("Enter number of points: "))
if N <= 0:
    print("N must be > 0")
else:
    inside = 0
    for i in range(N):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        if x*x + y*y <= 1:
            inside += 1
    pi = 4 * inside / N
    print(pi)