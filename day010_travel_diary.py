import json

traveler = input('Enter your name:')
destination= input ('Enter your destination:')
days=int(input('Enter number of days:'))
budget=float(input('Enter your budget:'))

transportation=float(input('Enter transportation cost:'))
food=float(input('Enter food cost:'))
hotel=float(input('Enter hotel cost:'))

trip={
    'traveler':traveler,
    'destination':destination,
    'days':days,
    'budget':budget,
    'expenses':{
        'transportation':transportation,
        'food':food,
        'hotel':hotel
    }
}

def display_trip_summary(trip):
    print ("==============Travel Diary==============")
    print (f'Traveler: {trip["traveler"]}')
    print (f'Destination: {trip["destination"]}')
    print (f'Days: {trip["days"]}')
    print (f'Budget: ${trip["budget"]:.2f}')
    print ('Expenses:')
    for expense, cost in trip['expenses'].items():
        print (f'{expense}: ${cost:.2f}')

with open('day010_travel_diary.json','w+') as file:
    json.dump(trip,file,indent=4)
    file.seek(0)
    content=file.read()
    print (f'The summary of trip is :\n {content}')

with open('day010_travel_diary.json','r') as file:
    trip_python=json.load(file)
    display_trip_summary(trip_python)

print ('test git again')