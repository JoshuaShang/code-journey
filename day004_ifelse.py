from ast import If


budget=1000
hotel=400
food=250
gas=100

total_spending=hotel+food+gas
if total_spending>budget:
    print("Over Budget")
elif total_spending==budget: 
    print("Exactly on Budget")
else:
    print("Within Budget")

Completed=True

if Completed:
    print("Trip Completed")
else:
    print("Trip Not Completed")

remaining_budget=budget-total_spending
if remaining_budget<200:
    print ('spending warnning')
else:
    print (f'remaining budget is {remaining_budget}')