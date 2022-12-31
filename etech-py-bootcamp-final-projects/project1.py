"""
**Problem 1:** Write a program to compute the grades of students. The test scores are to be read from a text file. Using
notepad, create a comma separated file with the data in it. Note that the data contains:

*firstname,lastname,id,test1,test2,final*

Bill,Bakar,11452,85,83,84

Sally,Simpson,11157,88,92,95

Mark,Mathews,111932,77,75,78

Cindy,Williams,1117,65,71,81

John,Jacobs,111873,67,72,68

Amy,Albright,11262,91,95,92

The weight of the test is 30%, the weight for the second test is 30%, and the weight for the final is 40%. The grades
breakown is:

`>` 90% A

85% - 89.99% A-

80% - 84.99% B+

70% - 79.99% B

60% - 69.99% C

50% - 59.99% D

The computed grades are to be stored in an output file as:

id    last name    grade
11262   Albright    A
111     John        B+
"""


def calculate_grades(input_file_name, output_file_name):
    f = open(input_file_name, 'r')  # Opening the input file in read mode (r)

    lines = f.readlines()

    results = []

    for line in lines:
        dataList = [item.strip() for item in str.split(line, ',') if item]  # Using list comprehension, to hold the
        # the various lines and the various fields split by comma using split() function

        score = (30 / 100 * int(dataList[3])) + (30 / 100 * int(dataList[4])) + (40 / 100 * int(dataList[5]))

        # Compare for the range to get the right grade

        if score > 90:
            grade = 'A'
        elif 85 <= score and score >= 89.99:
            grade = 'A-'
        elif 79 <= score and score >= 79.99:
            grade = 'B+'
        elif 70 <= score and score >= 79.99:
            grade = 'B'
        elif 60 <= score and score >= 69.99:
            grade = 'C'
        elif 50 <= score and score >= 59.99:
            grade = 'D'
        else:
            grade = 'F'

        results.append(dataList[2] + "  " + dataList[1] + "  " + grade)

        print(results)

    # Close the file since we are done reading from it
    f.close()

    # Now we open the output file in append mode (a)

    fw = open(output_file_name, 'a')

    # Write the result to the output file one line at a time fromt the results list
    for result in results:
        fw.write(result + '\n')

    fw.close()  # Close the output file when done writing to it


if __name__ == '__main__':
    print("Running Problem 1...")

    calculate_grades('student_grades.txt', 'result_grades.txt')

    print("Done! Output saved in result_grades.txt")
