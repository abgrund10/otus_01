"""
distribution of books among users
"""
import csv
import itertools
import urllib.request
import json

URL_1 = "https://raw.githubusercontent.com/konflic/front_example/master/data/books.csv"
URL_2 = "https://raw.githubusercontent.com/konflic/front_example/master/data/users.json"
urllib.request.urlretrieve(URL_1, "books.csv")
urllib.request.urlretrieve(URL_2, "users.json")

with open('users.json', mode='r', encoding='utf8') as users:
    result = []
    json_object = json.loads(users.read())
    for line in json_object:
        json_data = json.dumps(
            {'name': line['name'], 'gender': line['gender'],
             'address': line['address'], 'age': line['age']})
        result.append(json_data)
AMOUNT_OF_USERS = len(result)

with open('books.csv', encoding='utf8') as books:
    AMOUNT_OF_BOOKS = sum(1 for row in books)

# calc to distribute books
iteration = AMOUNT_OF_BOOKS // AMOUNT_OF_USERS  # calc equal distribution of books among users
residue = AMOUNT_OF_BOOKS % AMOUNT_OF_USERS  # calc how many users would have extra books

# add equal amount of books to users
if iteration > 0:
    ROW_ID_LOW = 0
    result_updated = []
    with open('books.csv', encoding='utf8') as books:
        csv_reader = csv.reader(books, delimiter=',')
        books.readline()
        for user in result:
            x = json.loads(user)
            books_array = []
            for row in itertools.islice(csv_reader, ROW_ID_LOW, ROW_ID_LOW + iteration):
                books_array.append(row)
            x['books'] = books_array
            result_updated.append(x)

if residue > 0:
    i = 0
    ROW_ID = iteration * AMOUNT_OF_USERS
    with open('books.csv', encoding='utf8') as books2:
        books2.readline()
        csv_reader = csv.reader(books2, delimiter=',')
        row = list(csv_reader)
        for user in result_updated[0:residue - 1]:
            x = json.loads(json.dumps(user))
            books_array = [x['books']]
            books_array.append(row[ROW_ID + i])
            x['books'] = books_array
            user['books'] = books_array
            i += 1

with open('result.json', mode='w', encoding='utf8') as f:
    json.dump(result_updated, f)
