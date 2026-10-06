
def calculate_average(marks):
    total = sum(marks)
    return total / len(marks)


marks = [80, 75, 90, 85, 70]

average = calculate_average(marks)

if average >= 40:
    print("Student passed")
else:
    print("Student failed")

print("Average marks:", average)
