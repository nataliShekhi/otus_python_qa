import json
from files import JSON_FILE_PATH
from files import CSV_FILE_PATH
from csv import DictReader

with open(JSON_FILE_PATH, "r", encoding="utf-8") as f:
    users = json.load(f)

with open(CSV_FILE_PATH, newline='', encoding="utf-8") as f:
    reader = DictReader(f)
    books = [
        {
            "title": row.get("Title"),
            "author": row.get("Author"),
            "pages": row.get("Pages"),
            "genre": row.get("Genre")
        }
        for row in reader
    ]

formatted_output = []
books_per_user = len(books) // len(users)
extra_books = len(books) % len(users)

book_index = 0

for i, user in enumerate(users):
    num_books = books_per_user + (1 if i < extra_books else 0)
    user_books = books[book_index:book_index + num_books]
    book_index += num_books
    formatted_output.append({
        "name": user["name"],
        "gender": user["gender"],
        "address": user["address"],
        "age": user["age"],
        "books": user_books
    })

with open("result.json", "w") as f:
    json.dump(formatted_output, f, indent=4)

