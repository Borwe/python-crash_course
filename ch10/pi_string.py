filename='pi_million_digits.txt'

with open(filename) as file_object:
    lines=file_object.readlines()

p1_string=''
for line in lines:
    p1_string+=line.strip()

birthday=input("Enter your birthday, in form mmddyy: ")
if birthday in p1_string:
    print('Your birthday apears in the first 1 million digits of pi')
else:
    print('Your birthday does not appear in the first million digits of pi.')