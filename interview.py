#  Task 3 print the sandeep

Name1 = 'SANDEEP'
for i in range(0 , len(Name1)):
    print(Name1[: -i])
for j in range(0, len(Name1)+1):
    print(Name1[:j])

def print_pattern(rows):
    for i in range(1, rows + 1):
        spaces = ' ' * (rows - i)
        stars = '* ' * i
        print(spaces + stars)

def reverse_pattern(rows):
    for i in range(rows - 1, 0, -1):
        spaces = ' ' * (rows - i)
        stars = '* ' * i
        print(spaces + stars)
        
print_pattern(11)
reverse_pattern(10)