import requests
r = requests.get("https://opentdb.com/api.php?amount=1&category=12&difficulty=easy&type=multiple")
# print(r.status_code)     # to ckek if request sent and received successfully
print(r.text)
print("--"*40)
print(type(r.text))   # it's a string (as it's in JSON (javascript object notation) format) Json format is object converted to string
print("--"*40)

import json # inbuilt module
question = json.loads(r.text)
print(type(question)) # now it's type has become a dictionary
print("--"*40)

import pprint
pprint.pprint(question)  # kind of work like the jsonview extension in chrome to read json files in a more clear way
print("--"*40)

print("Your question category is :-")
print(question['results'][0]['category'])
print("--"*40)

person = {'Name': 'John', 'Age': 19}
person_json = json.dumps(person)
print(type(person_json))             # converted dictionary to json
print('--'*40)
