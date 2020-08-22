# Note: GPA = (credit * grade) / total # of credits.
print('Welcome to the GPA Calculator.')
print('Please enter your letter grades, the "enter" key, then the amount of credits alloted to the course. *one course grade or credit per line.')
print('Enter a blank line by "done" when you are finished.')

# corresponding letter grade to point value
grades = {'A+':4.0, 'A':4.0, 'A-':3.7, 'B+':3.3, 'B':3, 'B-':2.7, 'C+':2.3, 'C':2.0, 'C-':1.7, 'D+':1.3, 'D':1, 'D-':0, 'F': 0}
credits = range(0,5)
total_credits = 0
num_courses = 0
total_gpa = 0
final_gpa = 0
done = False
while not done:
    grade = input('input letter grade for class: ')
    if grade == 'done':
        done = True
    elif grade not in grades:
        print('''Unknown value {0}; will be disregarded. 
        Please keep grade value between A+ - F''')
    else:
        num_courses += 1
        credit = int(input('input credit value for class: '))
        if credit not in credits:
            print('''Unknown value {0}; will be disregarded. 
            Please keep credit value between 1 and 5''')
        else:
            total_credits += credit
            total_gpa += (grades[grade]* credits[credit])

if num_courses > 0:
    final_gpa = total_gpa / total_credits
    print('Your GPA is:', final_gpa)
