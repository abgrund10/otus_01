import csv
import itertools
import urllib.request
import json
from itertools import islice

urllib.request.urlretrieve("https://raw.githubusercontent.com/konflic/front_example/master/data/books.csv", "books.csv")
urllib.request.urlretrieve("https://raw.githubusercontent.com/konflic/front_example/master/data/users.json", "users.json")

with open('users.json', 'r') as users:
    result = []
    json_object = json.loads(users.read())
    for line in json_object:
        json_data = json.dumps({'name': line['name'], 'gender': line['gender'], 'address': line['address'], 'age': line['age']})
        result.append(json_data)

amount_of_users = len(result)

with open('books.csv') as books:
    amount_of_books = sum(1 for row in books)

#cdistribute books
print('amount of books : ' + str(amount_of_books))
print('amount of users : ' + str(amount_of_users))
iteration = amount_of_books // amount_of_users
print('по сколько книг на юзера: ' + str(iteration))
ostatok = amount_of_books % amount_of_users
print('остаток от деления: '+ str(ostatok))

#add equal amount of books to users
if iteration > 0:
    lower_limit = 0
    upper_limit = iteration
    result_updated = []
    with open('books.csv') as books:
        csv_reader = csv.reader(books, delimiter=',')
        books.readline()
        for user in result:
            x = json.loads(user)
            books_array = []
            for row in itertools.islice(csv_reader, lower_limit, upper_limit):
                books_array.append(row)
            x['books'] = books_array
            result_updated.append(x)
#print('final array')
#print(result_updated)

if ostatok > 0:
    lower_limit = iteration * amount_of_users
    upper_limit = lower_limit + 1
    with open('books.csv') as books:
        csv_reader = csv.reader(books, delimiter=',')
        books.readline()
        for user in result_updated[0:ostatok]:
            user = json.dumps(user)
            x = json.loads(user)
            books_array = [x['books']]
            print('before')
            print(x['books'])
            for row in itertools.islice(csv_reader, lower_limit, upper_limit):
                books_array.append(row)
            x['books'] = books_array
            print('')
            print('update')
            print(x['books'])
print(result_updated)