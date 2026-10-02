destination=['Yosemite','Death Valley','Sequoia']

destination.remove('Sequoia')
destination.append('Lake Tahoe')
destination[1]='Joshua Tree'

for i in destination:
    print(i)