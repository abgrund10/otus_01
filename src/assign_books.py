import csv
import itertools
import urllib.request
import json

urllib.request.urlretrieve("https://raw.githubusercontent.com/konflic/front_example/master/data/books.csv", "books.csv")
urllib.request.urlretrieve("https://raw.githubusercontent.com/konflic/front_example/master/data/users.json",
                           "users.json")

with open('users.json', 'r') as users:
    result = []
    json_object = json.loads(users.read())
    for line in json_object:
        json_data = json.dumps(
            {'name': line['name'], 'gender': line['gender'], 'address': line['address'], 'age': line['age']})
        result.append(json_data)
amount_of_users = len(result)

with open('books.csv') as books:
    amount_of_books = sum(1 for row in books)

# distribute books
iteration = amount_of_books // amount_of_users  # calc equal distribution of books among users
residue = amount_of_books % amount_of_users  # calc how many users would have extra books

# add equal amount of books to users
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

if residue > 0:
    i = 0
    lower_limit = iteration * amount_of_users
    with open('books.csv') as books2:
        books2.readline()
        csv_reader = csv.reader(books2, delimiter=',')
        row = list(csv_reader)
        for user in result_updated[0:residue - 1]:
            x = json.loads(json.dumps(user))
            books_array = [x['books']]
            books_array.append(row[lower_limit + i])
            x['books'] = books_array
            user['books'] = books_array
            i += 1

with open('result.json', 'w') as f:
    json.dump(result_updated, f)
