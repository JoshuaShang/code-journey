# file=open('day009.txt','w+')
# file.write('this is the first line in the first create file\n')
# file.seek(0)
# txt=file.read()
# print (txt)
# file.close()

# with open ('day009.txt','w+') as file:
#     file.write('this is the second format of the writing file\n')
#     file.write('this is the second line in the second format of the writing file\n')
#     file.seek(0)
#     content=file.read()
# print (content)

# import json
# trip = {
#     "traveler": "Joshua",
#     "destination": "Yosemite",
#     "days": 2,
#     "budget": 700
# }

# with open('day009.json','w+') as file:
#     json.dump(trip,file,indent=4)
#     file.seek(0)
#     content=file.read()
#     print (content)

# with open('day009.json','w+') as file:
#     trip=json.loads(content)
#     trip['budget']=1000
#     print (trip)


# day 009 challenge
import json

trip = {
    "traveler": "Joshua",
    "destination": "Yosemite",
    "days": 2,
    "budget": 700
}

with open('day009_challenge.json','w') as file:
    json.dump(trip,file,indent=4)

with open('day009_challenge.json','r') as file:
    content=json.load(file)
    for i in content:
        print (f'{i} : {content[i]}')

