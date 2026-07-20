import csv

# try:
#     with open('users.csv', 'w', newline="") as file:
#         writer = csv.writer(file)
#         writer.writerow([['id','Name', 'Age'],
#                         ['1', 'Priya', '21'],
#                         ['2', 'Rishi', '22']])
# except Exception as e:
#         print(f"something wrong: {e}")

## reading csv file content
try:
    with open('users.csv', 'r', newline="") as file:
        reader = csv.reader(file)
        print(reader)
        for row in reader:
             print(row)
except Exception as e:
        print(f"something wrong: {e}")
        
