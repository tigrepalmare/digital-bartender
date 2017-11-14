import json
import requests


print(" Select the base for your drink \n 1 = Gin \n 2 = Rum \n 3 = Vodka \n 4 = Tequila ")
alcohol_choice = 0

while alcohol_choice == 0:
    alcohol_choice = int(input("Pick your poison by entering the number "))

    if alcohol_choice == 1:
        alchol = "gin"
    elif alcohol_choice == 2:
        alchol = "rum"
    elif alcohol_choice == 3:
        alchol = "vodka"
    elif alcohol_choice == 4:
        alchol = "tequila"
    else:
        alcohol_choice = 0
        print("We do not have that spirit, please enter a valid number")

print("You chose your drink to be " + alchol + " based!")

carbonation_choice = input("Would you like your drink carbonated?")

if carbonation_choice.lower().strip() == "yes":
    carbonation = "carbonated"
else:
    carbonation = "not/carbonated"
print(carbonation)

print(" How would you like your drink to taste?\n 1 = Bitter \n 2 = Fruity \n 3 = Sour \n 4 = Sweet")
taste_choice = 0

while taste_choice == 0:
    taste_choice = int(input("Pick a number"))

    if taste_choice == 1:
        taste = "bitter"
    elif taste_choice == 2:
        taste = "fruity"
    elif taste_choice == 3:
        taste = "sour"
    elif taste_choice == 4:
        taste = "sweet"
    else:
        taste_choice = 0
        print("That doesn't taste like anything! Try Again")

print(taste)

url = " http://addb.absolutdrinks.com/drinks" + "/withtype/" + alchol + "/" + carbonation + "/tasting/" + taste + "/?apiKey=replace with your API Key"

r = requests.get(url) #response i get from the URL after I autenticated with API key
parsed_json = json.loads(r.text) #parse the string to a json - standard notation for data-
print (parsed_json)
print (parsed_json.keys())
#print (json.dumps(parsed_json, indent=4, sort_keys=True))

first_result = parsed_json['result'][0]
print (first_result['name'])

for ingredient in first_result['ingredients']:
    print (ingredient['textPlain'])

#print (parsed_json['result'][1]['ingredients']['type'])
#print (parsed_json['result'][1]['descriptionPlain'])
