from json import JSONDecodeError

import requests

number = input("Enter a number: ")

try:
    print(int(number) *2)
except LookupError:
    print("Lookup error? This should never happen...")
except ValueError:
    print("You did not enter base 10 number! Try again.")

print("Hello")

r = requests.post("http://text-processing.com/api/sentiment", data={'text': 'hello world'})
try:
    label = r.json()['label']
    print(label)
except JSONDecodeError:
    print("We couldn't decode the JSON response!")
except KeyError:
    print("We got JSON back from sentiment analysis, but it not have a key 'label'.")
