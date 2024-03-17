num1 = 0
input_count = 0

user_num = int(input("Please enter a number: "))
while user_num != -1:
    num1 = num1 + user_num
    input_count += 1
    user_num = int(input("Please enter a number: "))
    if user_num == -1:
        print(num1/input_count)