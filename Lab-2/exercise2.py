# Lab 02 - Problem 1: Course Marks using Lists
marks = [75, 82, 48, 91, 63]

total = sum(marks)
average = total / len(marks)
highest = max(marks)
lowest = min(marks)

passed_count = 0
for mark in marks:
    if mark >= 50:
        passed_count += 1

print("--- Course Marks Summary ---")
print("Course Marks list :", marks)
print("Total Marks       :", total)
print(f"Average Mark      : {average:.2f}")
print("Highest Mark      :", highest)
print("Lowest Mark       :", lowest)
print("Passed Courses    :", passed_count)
print("Failed Courses    :", len(marks) - passed_count)

# Lab 02 - Problem 2: Weekend Temperatures using Tuples
weekend_temps = (24.5, 32.0, 26.0, 25.0, 34.5, 27.2)

labels = (
    "Saturday Morning", "Saturday Afternoon", "Saturday Night",
    "Sunday Morning",   "Sunday Afternoon",   "Sunday Night"
)

print("--- Weekend Temperature Readings ---")
for i in range(len(weekend_temps)):
    print(f"{labels[i]:20} : {weekend_temps[i]} °C")

highest_temp = max(weekend_temps)
lowest_temp = min(weekend_temps)

print("\n--- Temperature Summary ---")
print(f"Highest Temperature : {highest_temp} °C")
print(f"Lowest Temperature  : {lowest_temp} °C")

# Lab 02 - Problem 3: Word Analyzer
text = input("Enter a word or short sentence: ")

vowels = "aeiouAEIOU"
vowel_count = 0
space_count = 0

for char in text:
    if char in vowels:
        vowel_count += 1
    elif char == ' ':
        space_count += 1

total_chars = len(text)
other_chars = total_chars - (vowel_count + space_count)

print("\n--- Word Analyzer Report ---")
print(f"Analyzed Text        : \"{text}\"")
print(f"Total Characters     : {total_chars}")
print(f"Vowels (a, e, i, o, u): {vowel_count}")
print(f"Spaces               : {space_count}")
print(f"Other Characters     : {other_chars}")

# Lab 02 - Problem 4: Grade Calculator Function
def calculate_grade(marks):
    """
    Receives a list of marks, computes the average,
    and returns the corresponding letter grade.
    """
    if not marks:
        return 0.0, "No marks provided"
    
    average = sum(marks) / len(marks)
    
    if average >= 80:
        grade = "A"
    elif average >= 70:
        grade = "B"
    elif average >= 60:
        grade = "C"
    elif average >= 50:
        grade = "D"
    else:
        grade = "F"
        
    return average, grade

# Calling the function using a list of five marks
sample_marks = [85, 72, 90, 68, 81]
avg, grade = calculate_grade(sample_marks)

print("--- Grade Calculator Output ---")
print("Input Marks :", sample_marks)
print(f"Average     : {avg:.2f}")
print("Grade       :", grade)

# Lab 02 - Problem 5: Shopping Cart Processor
cart = [
    {"name": "Gaming Mouse", "price": 600, "quantity": 2},
    {"name": "Mechanical Keyboard", "price": 1200, "quantity": 1},
    {"name": "Mousepad", "price": 250, "quantity": 2},
    {"name": "USB Flash Drive", "price": 450, "quantity": 1}
]

# Calculate total cost using a loop
total_cost = 0
print("--- Shopping Cart Items ---")
for item in cart:
    item_total = item["price"] * item["quantity"]
    total_cost += item_total
    print(f"- {item['name']:20} : {item['quantity']} x ৳{item['price']} = ৳{item_total}")

# Discount function
def apply_discount(total):
    if total >= 2000:
        discount = total * 0.10
        return total - discount, discount
    return total, 0.0

final_amount, discount_given = apply_discount(total_cost)

print("\n--- Checkout Summary ---")
print(f"Subtotal       : ৳{total_cost:.2f}")
if discount_given > 0:
    print(f"Discount (10%) : -৳{discount_given:.2f}")
else:
    print("Discount (10%) : ৳0.00 (Minimum ৳2,000 required for discount)")
print(f"Final Total    : ৳{final_amount:.2f}")

# Lab 02 - Problem 6: Countdown using While Loop
num = int(input("Enter a non-negative integer: "))

while num < 0:
    print("Invalid input! Please enter a number >= 0.")
    num = int(input("Enter a non-negative integer: "))

print(f"\nCountdown from {num} to 0:")
current = num
while current >= 0:
    print(current)
    current -= 1

print("Countdown complete!")

# Lab 02 - Problem 7: Student Record Analyzer
students = [
    {"name": "Rahim", "department": "CSE", "marks": 85, "attendance": 92},
    {"name": "Karim", "department": "CSE", "marks": 48, "attendance": 76},
    {"name": "Sara",  "department": "DS",  "marks": 91, "attendance": 95},
    {"name": "Nadia", "department": "DS",  "marks": 67, "attendance": 84},
    {"name": "Hasan", "department": "CSE", "marks": 73, "attendance": 78}
]

# 1. Display each student's name and marks
print("--- Individual Student Records ---")
for s in students:
    status = "PASS" if s["marks"] >= 50 else "FAIL"
    print(f"Name: {s['name']:6} | Dept: {s['department']:3} | Marks: {s['marks']:2} | Status: {status}")

# 2. Count passed students (marks >= 50)
passed_students = sum(1 for s in students if s["marks"] >= 50)

# 3. Calculate class average
total_marks = sum(s["marks"] for s in students)
class_average = total_marks / len(students)

# 4. Identify student with highest mark
top_student = max(students, key=lambda s: s["marks"])

# 5. Display summary
print("\n--- Class Performance Analysis ---")
print(f"Total Students Evaluated : {len(students)}")
print(f"Passed Students (>= 50)  : {passed_students}")
print(f"Failed Students (< 50)   : {len(students) - passed_students}")
print(f"Class Average Mark       : {class_average:.2f}")
print(f"Highest Mark Achiever    : {top_student['name']} ({top_student['marks']} marks, {top_student['department']} department)")

# Lab 02 - Problem 8: Product Inventory Summary
products = [
    {"name": "Notebook",  "price": 120, "quantity": 3},
    {"name": "Pen",       "price": 20,  "quantity": 5},
    {"name": "USB Drive", "price": 850, "quantity": 2},
    {"name": "Mouse",     "price": 650, "quantity": 1}
]

total_inventory_value = 0
highest_line_total = -1
highest_product = None

print("--- Product Line Totals ---")
# 1. Calculate each product's line total (price * quantity)
for p in products:
    line_total = p["price"] * p["quantity"]
    total_inventory_value += line_total
    print(f"Product: {p['name']:10} | Price: ৳{p['price']:4} | Qty: {p['quantity']:2} | Line Total: ৳{line_total}")

    if line_total > highest_line_total:
        highest_line_total = line_total
        highest_product = p

# 2. Display inventory summary
print("\n--- Inventory Summary ---")
print(f"Total Inventory Value        : ৳{total_inventory_value}")
print(f"Product with Highest Total   : {highest_product['name']} (Line Total: ৳{highest_line_total})")
