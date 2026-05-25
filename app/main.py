from db.db import SessionLocal
from db.crud import get_categories, get_books

session = SessionLocal()

print("Категории книг:")
categories = get_categories(session)

for category in categories:
    print(f"{category.id}. {category.title}")

print("\nКниги в базе данных:")
books = get_books(session)

for book in books:
    print(
        f"{book.id}. {book.title} | "
        f"{book.description} | "
        f"Цена: {book.price} | "
        f"Категория: {book.category.title}"
    )

session.close()
