import os
from operator import itemgetter

def main():
    students = get_students()

    print(students)

    students = sorted(students, key=itemgetter(1))

    print_students(students)


def get_file_name():
    file_name = input("Enter name of file, include extension: ")

    if(not os.path.exists(file_name)):
        print("File does not exist")
        return get_file_name()
    
    return file_name

def get_students():
    students = []

    file_name = get_file_name()

    student_file = open(file_name)

    line = student_file.readline()

    print(student_file)
    print(line)

    while not line == "":
        line = line.replace("\n", "")

        data_list = line.split("#")
        name = data_list[0]
        class_standing = data_list[1]
        grade = data_list[2]

        students.append([name, class_standing, grade])

        line = student_file.readline()

    student_file.close()
    return students

def print_students(students):
    
    for student in students:
        print(f"{student[0]:<15} {student[1]:>10} {student[2]:>5}")
        
main()