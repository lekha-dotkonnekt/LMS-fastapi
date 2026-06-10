from fastapi import APIRouter, HTTPException
from typing import List
from uuid import uuid4
from schemas import BookCreate, Book, BookUpdate

router = APIRouter(prefix="/books", tags=["books"])

# In-memory storage for demo purposes
books_db = {}


@router.post("/", response_model=Book)
def create_book(book: BookCreate):
    book_id = str(uuid4())
    b = Book(id=book_id, **book.dict())
    books_db[book_id] = b
    return b


@router.get("/", response_model=List[Book])
def list_books():
    return list(books_db.values())


@router.get("/{book_id}", response_model=Book)
def get_book(book_id: str):
    b = books_db.get(book_id)
    if not b:
        raise HTTPException(status_code=404, detail="Book not found")
    return b


@router.put("/{book_id}", response_model=Book)
def update_book(book_id: str, book: BookUpdate):
    existing = books_db.get(book_id)
    if not existing:
        raise HTTPException(status_code=404, detail="Book not found")
    updated = existing.copy(update=book.dict(exclude_unset=True))
    books_db[book_id] = updated
    return updated


@router.delete("/{book_id}", status_code=204)
def delete_book(book_id: str):
    if book_id in books_db:
        del books_db[book_id]
    else:
        raise HTTPException(status_code=404, detail="Book not found")
