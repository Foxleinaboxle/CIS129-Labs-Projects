#Vixen Hinkle
#Cis_129_Modual_11_Lab
#Class Average

#presented a class-average script in which you could enter any number of
#grades followed by a sentinel value, then calculate the class average. Another
#approach would be to read the grades from a file. In an IPython session, write
#code that enables you to store any number of grades into a grades.txt plain text file.
print('9.1')
with open('grades.txt', mode='w') as grades:
    grades.write('1 Johnathan 56.48\n')
    grades.write('2 Marcus 89.80\n')
    grades.write('3 Olivia 100.00\n')
    grades.write('4 Steven 26.89\n')
    grades.write('5 Genna 79.24\n')

#print the open log
print(grades)

#IPython session, write code that reads the grades from the grades.txt file
#you created in the previous exercise. Display the individual grades and their
#total, count and average.
print('9.2')
with open('grades.txt', mode='r') as grades:
    print(f'{"Period":<10}{"Name":<10}{"Grade":>10}')
    for record in grades:
        period, name, grade = record.split()
        print(f'{period:<10}{name:<10}{grade:>10}')

#structor teaches a class in which each student takes three exams.
#The instructor would like to store this information in a file named grades.csv for later use.
#Write code that enables an instructor to enter each student’s first name and last name as strings
#and the student’s three exam grades as integers.
#Use the csv module to write each record into the grades.csv file.
#Each record should be a single line of text in the following CSV format:
#firstname,lastname,exam1grade,exam2grade,exam3grade
print('9.3')
grades = open('grades.txt', 'r')

temp_file = open('temp_file.txt', 'w')

with grades, temp_file:
    for record in grades:
        period, name, grade = record.split()
        Periodselect = input('Wich period (1-5) do you want to select? ')
        if period != Periodselect:
            temp_file.write(record)
        else:
            Logupdate = input('Please enter the updated information (firstname,lastname,exam1grade,exam2grade,exam3grade): ')
            new_record = ' '.join([Logupdate])
            temp_file.write(new_record + '\n')
