print('Hi there Coursera, this is my code running!')

'''
2.2 Write a program that uses input to prompt a user for their name and then welcomes them. Note that input will pop up a dialog box. Enter Sarah in the pop-up box when you are prompted so your output will match the desired output. '''

name_input = input('What is your name?: ')
print('Hello', name_input)

'''
2.3 Write a program to prompt the user for hours and rate per hour using input to compute gross pay. Use 35 hours and a rate of 2.75 per hour to test the program (the pay should be 96.25). You should use input to read a string and float() to convert the string to a number. Do not worry about error checking or bad user data. ''' 


rate = float(input('What is your rate per hour: '))

hourly = float(input('How many hours have you worked: '))

pay = rate * hourly

print(pay)



'''
Write a program to prompt the user for hours and rate per hour using input to compute gross pay. Pay the hourly rate for the hours up to 40 and 1.5 times the hourly rate for all hours worked above 40 hours. Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75). You should use input to read a string and float() to convert the string to a number. Do not worry about error checking the user input - assume the user types numbers properly.
'''

try:
    rate = float(input('what is your rate per hour: '))
    hourly = float(input('How many hours have you worked: '))
except:
    print('Error please enter numeric input')

cap = rate * 40
over_hours = hourly - 40
new_rate = rate * 1.5

if hourly > 40:
    overtime = new_rate * over_hours
    overall_pay = cap + overtime
    print(overall_pay)
else:
    print(rate * hourly)


''' 
Write a program to prompt for a score between 0.0 and 1.0. If the score is out of range, print an error. If the score is between 0.0 and 1.0, print a grade using the following table:
Score Grade
>= 0.9 A
>= 0.8 B
>= 0.7 C
>= 0.6 D
< 0.6 F
If the user enters a value out of range, print a suitable error message and exit. For the test, enter a score of 0.85.
'''


score = float(input('Enter a user score (between 0.0 - 1.0): '))
print(score)
    
if score > 1.0 or score < 0:
    print('Input error: score does not sit between given range. Please try again')
elif score >= 0.9:
    print('A')
elif score >= 0.8:
    print('B')
elif score >= 0.7:
    print('C')
elif score >= 0.6:
    print('D')
else:
    print('F')



'''
Write a program to prompt the user for hours and rate per hour using input to compute gross pay. Pay should be the normal rate for hours up to 40 and time-and-a-half for the hourly rate for all hours worked above 40 hours. Put the logic to do the computation of pay in a function called computepay() and use the function to do the computation. The function should return a value. Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75). You should use input to read a string and float() to convert the string to a number. Do not worry about error checking the user input unless you want to - you can assume the user types numbers properly. Do not name your variable sum or use the sum() function.
'''

try:
    rate = float(input('what is your rate per hour: '))
    hourly = float(input('How many hours have you worked: '))
except:
    print('Error please enter numeric input')


def computepay(rate, hours):

    cap = rate * 40
    over_hours = hours - 40
    new_rate = rate * 1.5

    if hourly > 40:
        overtime = new_rate * over_hours
        overall_pay = cap + overtime
        return overall_pay
    else:
        pay = rate * hours
        return pay

test_1 = computepay(10.50, 39)
test_2 = computepay(rate, hourly)

print(test_1)
print(test_2)



''' 
Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'. Once 'done' is entered, print out the largest and smallest of the numbers. If the user enters anything other than a valid number catch it with a try/except and put out an appropriate message and ignore the number. Enter 7, 2, bob, 10, and 4 and match the output below. 
'''

smallest = None
largest = None
num_list = []

while True:
    try:
        user_input = input("Enter a number, type end when you are finished: ")
        if user_input.lower() == "done":
            break
        user_input = int(user_input)
        num_list.append(user_input)             
    except:
        print('Invalid input')
        break
        

for num in num_list:
    if smallest is None:
        smallest = num
    elif num < smallest:
        smallest = num
    elif largest is None:
        largest = num
    elif num > largest:
        largest = num

print(num_list)
print("Maximum is", largest)
print("Minimum is", smallest)


num = 54
string = 'This is a string'

print(dir(num))
print(dir(string))

'''
Write code using find() and string slicing (see section 6.10) to extract the number at the end of the line below. Convert the extracted value to a floating point number and print it out. 
'''



text = "X-DSPAM-Confidence:    0.8475";

locate = text.find('0')
print(locate) # 23 index
extracted = text[23:]
extracted = float(extracted)


'''
Write a program that prompts for a file name, then opens that file and reads through the file, and print the contents of the file in upper case. Use the file words.txt to produce the output below.
You can download the sample data at
''' 

new_file = input('Enter file name: ')
file_open = open(new_file)
read = file_open.read()
read = read.strip()
print(read.upper())



'''
Write a program that prompts for a file name, then opens that file and reads through the file, looking for lines of the form:
X-DSPAM-Confidence:    0.8475
Count these lines and extract the floating point values from each of the lines and compute the average of those values and produce an output as shown below. Do not use the sum() function or a variable named sum in your solution.
You can download the sample data at http://www.py4e.com/code3/mbox-short.txt when you are testing below enter mbox-short.txt as the file name.
'''

line_count = 0
count = 0
line_list = []

new_file = input('Enter file name: ')
file = open(new_file)

for line in file:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    else:
        line_count = line_count + 1
        locate = line.find(':') # located at index 18
        extracted = line[19:].strip()
        extracted = extracted.strip("\\")
        convert = float(extracted)
        line_list.append(convert)


for num in line_list:
    count = count + num
    average = count / len(line_list)


print("Average spam confidence:", average)




'''
8.4 Open the file romeo.txt and read it line by line. For each line, split the line into a list of words using the split() method. The program should build a list of words. For each word on each line check to see if the word is already in the list and if not append it to the list. When the program completes, sort and print the resulting words in alphabetical order. ''' 



lst = []
filename = input("Enter file name: ")
fileopen = open(filename)
for line in fileopen:
    line = line.rstrip()
    line = line.rstrip("}")
    split = line.split()
    for word in split:
        if word not in lst:
            print(word)
            lst.append(word)
        else:
            continue
lst.sort()
print(lst)



'''
8.5 Open the file mbox-short.txt and read it line by line. When you find a line that starts with 'From ' like the following line:
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
You will parse the From line using split() and print out the second word in the line (i.e. the entire address of the person who sent the message). Then print out a count at the end.
Hint: make sure not to include the lines that start with 'From:'.
'''

count = 0
fname = input("Enter file name: ")
fh = open(fname)

for line in fh:
    line = line.rstrip()
    if line.startswith('From '):
        count = count + 1
        line = line.split()
        print(line[1])

print("There were", count, "lines in the file with From the first word")



''' Get() method: The pattern of checking to see if a key is already in the dictionary and assuming the default value if the key is not there. '''
# Example of Get() method:

counts = dict()
names = ['csev', 'cwen', 'csev', 'zqian', 'cwen']

for name in names:
    counts[name] = counts.get(name, 0) + 1
print(counts)

# Other examples:

counts = dict()

text = input('Enter string of text: ')

words = text.split()

print('Words:', words)
print('couting....')

for word in words:
    counts[word] = counts.get(word,0) + 1

print('Counts: ', counts)




''' 9.4 Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages. The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer. '''


name = input("Enter file:")
if len(name) < 1 : name = "words.txt.rtf"
fh = open(name)
names = []

for line in fh:
    line = line.rstrip()
    if line.startswith('From '):
        line = line.split()
        line = line[1]
        names.append(line)        

counts = dict()
highest_name = None
highest_count = None

for name in names:
    counts[name] = counts.get(name, 0) + 1


for name,count in counts.items():
    if highest_count is None or count > highest_count:
        highest_name = name
        highest_count = count
    
print(highest_name, highest_count)




''' 10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below. ''' 

# example code: 
'''
fhand = open('romeo.txt')
counts = dict()

for line in fhan# 
    words = line# .split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1

lst = list()
for key,value in counts.items():
    newtup = (value,key)
    lst.append(newtup)

lst = sorted(lst, reverse= True)
'''


name = input("Enter file:")
if len(name) < 1 : name = "words.txt.rtf"
fh = open(name)
hour_count = dict()


for line in fh:
    line = line.rstrip()
    if line.startswith('From '):
        line = line.split()
        line = line[5].split(':')
        line = line[0]
        hour_count[line] = hour_count.get(line, 0) + 1

print(hour_count)

lst = list()

for key,value in hour_count.items():
    newtup = (key, value)
    lst.append(newtup)

lst = sorted(lst)
for key, val in lst:
    print(key, val)




