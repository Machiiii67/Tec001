#1
def countt_(filename):
    count = 0
    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            if line.strip() != "":
                count += 1
    return count
file_path = input("Nhập đường dẫn file: ")
try:
    result = countt_(file_path)
    print("Số dòng không rỗng là:", result)
except FileNotFoundError:
    print("Không tìm thấy file!")
#2
def findd(filename, keyword):
    line_numbers = []
    with open(filename, "r", encoding="utf-8") as file:
        for index, line in enumerate(file, start=1):
            if keyword in line:
                line_numbers.append(index)
    return line_numbers

file_path = input("Nhập đường dẫn file: ")
keyword = input("Nhập keyword cần tìm: ")
try:
    result = findd(file_path, keyword)
    print("Keyword xuất hiện ở các dòng:", result)
except FileNotFoundError:
    print("Không tìm thấy file!")
#3
file_path = input("Nhập đường dẫn đến file của bạn: ")
total = 0
count = 0
try:
    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            if line:
                parts = line.split(",")
                name, score = parts[0], parts[-1]
                total += float(score)
                count += 1
    if count > 0:
        average = total / count
        print("Điểm trung bình là:", average)
    else:
        print("File không có dữ liệu hợp lệ.")
except FileNotFoundError:
    print("Không tìm thấy file. Hãy kiểm tra lại đường dẫn.")
except Exception as e:
    print("Có lỗi xảy ra:", e)
#4
def caesar(filename, shift, direction):
    s = shift if direction == 'right' else -shift
    result = ''
    f = open(filename, 'r')
    for line in f:
        for ch in line:
            if ch.isupper():
                result += chr((ord(ch) + s) % 26 + 65)
            elif ch.islower():
                result += chr((ord(ch) + s) % 26 + 97)
            else:
                result += ch
    f.close()
    return result

filename = input("Nhap duong dan file: ")
shift = int(input("Nhap so vi tri dich: "))
direction = input("Nhap huong dich (right/left): ")

try:
    result = caesar(filename, shift, direction)
    output_file = input("Nhap ten file de luu ket qua: ")
    with open(output_file, 'w') as f:
        f.write(result)
    print("Da luu vao", output_file)
except FileNotFoundError:
    print("Khong tim thay file!")
except Exception as e:
    print("Co loi xay ra:", e)