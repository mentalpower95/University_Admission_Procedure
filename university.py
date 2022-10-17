with open("applicant_list_7.txt") as file:
    data = [line.split() for line in file]

number_of_students = int(input())

for i in data:
    for number in range(2, 7):
        i[number] = float(i[number])

departments = ["Biotech", "Chemistry", "Engineering", "Mathematics", "Physics"]
exam = {"Biotech": (2, 3), "Chemistry": (3, 3), "Engineering": (4, 5), "Mathematics": (4, 4), "Physics": (2, 4)}
final = {key: [] for key in departments}
used = []

for i in range(7, 10):
    for department in departments:
        sorted_data = sorted(data, key=lambda x: (-(max([(x[exam[department][0]] + x[exam[department][1]]) / 2, x[6]])),
                                                  x[0], x[1]))
        for student in sorted_data:
            if student[i] == department and len(final[department]) < number_of_students and student not in used:
                score = (student[exam[department][0]] + student[exam[department][1]]) / 2
                final[department].append([student[0], student[1], max([score, student[6]])])
                used.append(student)

for department in departments:
    new_file = open(f"{department}.txt", "w")
    group = sorted(final[department], key=lambda x: (-x[2], x[0], x[1]))
    for s in group:
        new_file.write(f"{s[0]} {s[1]} {s[2]}\n")
    new_file.close()
