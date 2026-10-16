# Lab 01 - Activity 01: Variables
student_name = "Rahim"
student_id = "24-12345-1"
age = 21
cgpa = 3.50
department = "Data Science"

print("Student Name :", student_name)
print("Student ID   :", student_id)
print("Age          :", age)
print("CGPA         :", cgpa)
print("Department   :", department)

# Lab 01 - Activity 02: Data Types
name = "Rahim"
age = 21
cgpa = 3.50
is_student = True

print("Data type of name       :", type(name))
print("Data type of age        :", type(age))
print("Data type of cgpa       :", type(cgpa))
print("Data type of is_student :", type(is_student))

# Lab 01 - Activity 03: User Input
name = input("Enter your name: ")
age = input("Enter your age: ")
department = input("Enter your department: ")

print("\nHello", name)
print("You are", age, "years old.")
print("You study " + department + ".")

# Lab 01 - Activity 04: Basic Arithmetic
a = 25
b = 4

print("Sum:       ", a + b)
print("Difference:", a - b)
print("Product:   ", a * b)
print("Division:  ", a / b)
print("Remainder: ", a % b)

# Lab 01 - Problem 1: Numeric Inputs and Arithmetic Operations
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

sum_result = num1 + num2
diff_result = num1 - num2
product_result = num1 * num2

print("\n--- Arithmetic Results ---")
print(f"First Number : {num1}")
print(f"Second Number: {num2}")
print(f"Sum          : {sum_result}")
print(f"Difference   : {diff_result}")
print(f"Product      : {product_result}")

if num2 != 0:
    quotient_result = num1 / num2
    print(f"Quotient     : {quotient_result:.4f}")
else:
    print("Quotient     : Undefined (Division by zero is not allowed)")

    # Lab 01 - Problem 2: Formatted Student Profile
name = input("Enter student name: ")
student_id = input("Enter student ID (e.g., 24-12345-1): ")
age = int(input("Enter age: "))
department = input("Enter department: ")
cgpa = float(input("Enter CGPA (0.00 - 4.00): "))

print("\n" + "=" * 45)
print("     AIUB STUDENT ACADEMIC PROFILE")
print("=" * 45)
print(f"  Name        : {name}")
print(f"  Student ID  : {student_id}")
print(f"  Age         : {age} years")
print(f"  Department  : {department}")
print(f"  CGPA        : {cgpa:.2f} / 4.00")
print("=" * 45)

# Lab 01 - Problem 3: Temperature Conversion
celsius = float(input("Enter temperature in Celsius (°C): "))

# Formulas from manual:
fahrenheit = (celsius * 9 / 5) + 32
kelvin = celsius + 273.15

print("\n--- Temperature Conversion Results ---")
print(f"Celsius    : {celsius:.2f} °C")
print(f"Fahrenheit : {fahrenheit:.2f} °F")
print(f"Kelvin     : {kelvin:.2f} K")

# Lab 01 - Problem 4: Course Performance Analyzer
student_name = input("Enter student name: ")

marks = []
for i in range(1, 6):
    mark = float(input(f"Enter mark for course {i}: "))
    marks.append(mark)

total_marks = sum(marks)
average_mark = total_marks / len(marks)
highest_mark = max(marks)
lowest_mark = min(marks)

# Pass mark is 50 or higher
passed_courses = sum(1 for m in marks if m >= 50)
failed_courses = len(marks) - passed_courses

print("\n" + "=" * 45)
print(f"  ACADEMIC SUMMARY: {student_name}")
print("=" * 45)
print(f"  Marks Obtained   : {marks}")
print(f"  Total Marks      : {total_marks:.2f}")
print(f"  Average Mark     : {average_mark:.2f}")
print(f"  Highest Mark     : {highest_mark:.2f}")
print(f"  Lowest Mark      : {lowest_mark:.2f}")
print(f"  Passed Courses   : {passed_courses} out of {len(marks)}")
print(f"  Failed Courses   : {failed_courses} out of {len(marks)}")
print("=" * 45)

