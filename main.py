Question #1
def ch2_sec17_ex13():
number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))
result = number1 + number2
print(f"The sum of {number1} and {number2} is {result}")

Question #2
def ch6_sec10_ex1():
weather = ["Sunny", "Cloudy", "Rainy", "Snowy"]
for item in weather:
    length = len(item)
    first_char = item[0]
    last_char = item[-1]
    print(f"Item: {item}, Length: {length}, First Character: {first_char}, Last Character: {last_char}")

Question #3
def ch7_sec14_ex11():
num_students = ["Alex", "Elvir", "Emin", "Stefan", "Dzenan"]
students_entered = 0
for student in num_students:
    students_entered += 1
    print(f"Hello, {student}!")
    print(f"{students_entered} students have entered the room so far.")
Question #4
def sum_of_squares(num_list):
result = 0
    for num in num_list:
        result = result + (num * num)
    return result
Question #5
def main():
    nums = [2, 3, 4]
    result = sum_of_squares(nums)
    print(result)





