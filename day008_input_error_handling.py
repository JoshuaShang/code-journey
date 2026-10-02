name=input('what is your name?')
destination=input('where arre you travelling?')

try:
    budget=float(input('Enter your budget:'))
    hotel=float(input('Enter hotel cost:'))
    food=float(input('Enter food cost:'))
    transportation=float(input('Enter transportation cost:'))
except ValueError:
    print ('Please enter a valid number')

def calculate_trip_cost(hotel,food,transportation):
    return hotel+food+transportation
def check_budget(total_cost, budget):
    if total_cost<=budget:
        print (f'under budget! You have ${budget-total_cost} left.')
    else:
        print (f'over budget! You need ${total_cost-budget} more.')

total_cost=calculate_trip_cost(hotel,food,transportation)


print (f'Traveler is {name}')
print (f'Destination is {destination}')
print (f'Total expense is ${total_cost:.2f}')
check_budget(total_cost,budget)