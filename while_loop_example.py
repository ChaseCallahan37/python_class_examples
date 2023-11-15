def get_decision():
    decision = input('Would you like to enter a grade ("yes/no")? ').lower()
    
    while  not(decision == "yes" or decision == "no"):
        print("The decision has to be yes or no")
        decision = input('Would you like to enter a grade ("yes/no")? ').lower()
    
    return decision


def get_grade():
    grade = input("Enter a grade (0-100): ")
    
    while not is_valid(grade):
        grade = input("Enter a grade (0-100): ")

    return int(grade)
        

def is_valid(value):
    try:
        int(value)
    except ValueError:
        print("The grade should be an integer!")
        return False
    
    if 0 <= int(value) <=100:
        return True
    else:
        print("The grade should be between 0 and 100, inclusive!")
        return False


#  Driver code
decision = get_decision()
print(decision)

count = 0
total_grade = 0

while decision == "yes":
    grade = get_grade()
    count += 1
    total_grade += grade
    decision = get_decision()

print(f"The average grade is {total_grade/count}")
