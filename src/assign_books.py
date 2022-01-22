import urllib.request

import json

urllib.request.urlretrieve("https://raw.githubusercontent.com/konflic/front_example/master/data/books.csv", "books.csv")
urllib.request.urlretrieve("https://raw.githubusercontent.com/konflic/front_example/master/data/users.json", "users.json")

with open('users.json', 'r') as users:
    result = []
    json_object = json.loads(users.read())
    for line in json_object:
        json_data = json.dumps({'name': line['name'], 'gender': line['gender'], 'address': line['address'], 'age': line['age'], 'books': 0 })
        result.append(json_data)
print(result)

amount_of_users = len(result)

with open('books.csv', 'r') as books:
    json_object = books.read()
    amount_of_books = len(json_object)

