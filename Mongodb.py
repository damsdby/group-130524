from pymongo.mongo_client import MongoClient

from config import USER_NAME, PASSWORD

uri = f"mongodb+srv://{USER_NAME}:{PASSWORD}>@hillel1.pbl2t.mongodb.net/?retryWrites=true&w=majority&appName=hillel1"

# Create a new client and connect to the server
client = MongoClient(uri)

db = client['books_database']

fantasy_books = db['fantasy_books']
school_literature = db['school_literature']

fantasy_books.insert_one({'title': 'Гра Престолів', 'price': '350', 'year': '1996', 'pages': '690'})

school_literature.insert_many([
    {'title': 'Історія України', 'class': 9, 'pages': 200},
    {'title': 'Історія середніх віків', 'class': 9, 'pages': 180},
    {'title': 'Українська мова', 'class': 9, 'pages': 220},
    {'title': 'Математика', 'class': 9, 'pages': 300},
    {'title': 'Література', 'class': 9, 'pages': 150},
])


history_books = school_literature.find({'title': {'Історія'}})

for book in history_books:
    print(book)
