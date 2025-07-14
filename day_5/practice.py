input_str = "11 55 99"

# Step 1: Extract only digits and spaces
only_digits_spaces = ""
for char in input_str:
    if char.isdigit() or char.isspace():
        only_digits_spaces += char

print("Only digits and spaces:", only_digits_spaces)

# Step 2: Make them into a list of numbers
# Use split() to split by spaces, then filter out empty strings
numbers = only_digits_spaces.split()
print("Numbers in string:", numbers)
mm=[]
for i in numbers:
    if int(i)>=11:
        mm.append(i)
print(mm)

# # Step 3: Extract only 2-digit numbers
# two_digit_numbers = []
# for num in numbers:
#     if len(num) == 2:
#         two_digit_numbers.append(int(num))

# print("2-digit numbers:", two_digit_numbers)