destination = ['Yosemite', 'Death Valley', 'Sequoia']
for i in range (len(destination)):
    print (f'Destination {i+1}:{destination[i]}')

total=0
expenses = [120, 45, 80, 35]
for i in range(len(expenses)):
    total+=expenses[i]
print (f'Total expense is {total}')

total=0
expenses = [120, 45, 80, 35]
for i in range(len(expenses)):
    if expenses[i]>100:
        print(f'expenses[i] is greater than 100')
    else:
        print(f'expenses[i] is equal or less than 100')
print (f'Total expense is {total}')
