# Dependencies
import requests
import json
import random

# Base URL for GET requests to retrieve number/date facts
url = "http://numbersapi.com/"

# Ask the user what kind of data they would like to search for
question = ("What kind of fact would you like? "
            "[Trivia, Math, or Year] ")
kind_of_search = input(question)

if(kind_of_search.lower() == "year"):
    number = input('What year would you like to search for (enter a number or "random")? ')
    if (number == 'random'):
        number = random.randint(0,2019)
else:
    number = input('What number would you like to search for (enter a number or "random")? ')
    if (number == 'random'):
        number = random.randint(0,10000)
    
# Make an API call to the API and get the JSON object
response = requests.get(f'{url}{number}/{kind_of_search.lower()}?json').json()

# Print the fact stored within the response
print(response["text"])