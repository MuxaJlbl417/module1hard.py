students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = list(students)
students.sort()
students_one = sum(grades[0]) / len(grades[0])
students_two = sum(grades[1]) / len(grades[1])
students_three = sum(grades[2]) / len(grades[2])
students_four = sum(grades[3]) / len(grades[3])
students_five = sum(grades[4]) / len(grades[4])
total = {}
total = {students[0]:students_one, students[1]:students_two, students[2]:students_three, students[3]:students_four, students[4]:students_five}
print(total)