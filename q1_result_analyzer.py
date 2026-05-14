name = "Pranav Vasisht Miryan"
rollno = "05H4"
marks = [75.5, 35.0, 70.0, 82.5, 50.0]

t = sum(marks)
avg = t / len(marks)

if avg >= 90:
    grade = "A"
elif avg >= 75:
    grade = "B"
elif avg >= 60:
    grade = "C"
elif avg >= 40:
    grade = "D"
else:
    grade = "Fail"

print(f"Student: {name} (Roll: {rollno})")
print(f"Total: {t}, Average: {avg}")
print(f"Grade: {grade}")

below_40 = []

for i in range(len(marks)):
    if marks[i] < 40:
        below_40.append(f"Subjects: {i+1}")

if below_40:
    print("Subjects below 40:", ", ".join(below_40))
else:
    print("Subjects below 40: 0")