with open("applicant_list_7.txt") as file:
    data = [line.split() for line in file]

# DATA STRUCTURE
# 0 First Name
# 1 Surname
# 2 Physics Exam
# 3 Chemistry Exam
# 4 Math Exam
# 5 PC Exam
# 6 University Admission Exam
# 7 First Choice Department
# 8 Second Choice Department
# 9 Third Choice Department

number_of_students = int(input())  # Max number of students accepted to each department

for i in data:
    for number in range(2, 7):
        i[number] = float(i[number])

departments = ["Biotech", "Chemistry", "Engineering", "Mathematics", "Physics"]
exam = {"Biotech": (2, 3), "Chemistry": (3, 3), "Engineering": (4, 5), "Mathematics": (4, 4), "Physics": (2, 4)}  # Combinations of exams needed for dpmnt
final = {key: [] for key in departments}
used = []

for i in range(7, 10):
    for department in departments:
        sorted_data = sorted(data, key=lambda x: (-(max([(x[exam[department][0]] + x[exam[department][1]]) / 2, x[6]])), x[0], x[1]))  # Sorting by points, name and surname
        for student in sorted_data:
            if student[i] == department and len(final[department]) < number_of_students and student not in used:  # Assigning student to deparment (if dpmnt not full yet)
                score = (student[exam[department][0]] + student[exam[department][1]]) / 2
                final[department].append([student[0], student[1], max([score, student[6]])])
                used.append(student)

for department in departments:  # Transfering data from dict to external files
    new_file = open(f"{department}.txt", "w")
    group = sorted(final[department], key=lambda x: (-x[2], x[0], x[1]))
    for s in group:
        new_file.write(f"{s[0]} {s[1]} {s[2]}\n")
    new_file.close()
