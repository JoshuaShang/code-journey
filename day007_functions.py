def calculate_trip_cost(hotel,food,transportation):
    return hotel+food+transportation

def check_budget(total_cost, budget):
    if total_cost<=budget:
        print (f'under budget! You have ${budget-total_cost} left.')
    else:
        print (f'over budget! You need ${total_cost-budget} more.')

hotel=350
food=180
transportation=120
total_cost=calculate_trip_cost(hotel,food,transportation)

print (f'Total trip cost is ${total_cost}')

budget=700

check_budget(total_cost,budget)
