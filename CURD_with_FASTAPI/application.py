
#  ------------------------------------------------------------------------------------------------
# This is an API. which are having four end points to perform the CRUD operation with SQLite
#  ------------------------------------------------------------------------------------------------
from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

import crud
import model
import schema
from db_handler import SessionLocal, engine

model.Base.metadata.create_all(bind=engine)

# initiating app
app = FastAPI(
    title="Books Details",
    description="You can perform CRUD operation by using this API",
    version="1.0.0"
)


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get('/retrieve_all_books_details', response_model=List[schema.Book])
def retrieve_all_books_details(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    books = crud.get_movies(db=db, skip=skip, limit=limit)
    return books


@app.post('/add_new_books', response_model=schema.BookAdd)
def add_new_book(book: schema.BookAdd, db: Session = Depends(get_db)):
    book_id = crud.get_book_by_book_id(db=db, movie_id=book.book_id)
    if book_id:
        raise HTTPException(status_code=400, detail=f"Book id {book.book_id} already exist in database: {book_id}")
    return crud.add_book_details_to_db(db=db, book=book)


@app.delete('/delete_book_by_id')
def delete_book_by_id(sl_id: int, db: Session = Depends(get_db)):
    details = crud.get_book_by_id(db=db, sl_id=sl_id)
    if not details:
        raise HTTPException(status_code=404, detail=f"No record found to delete")

    try:
        crud.delete_book_details_by_id(db=db, sl_id=sl_id)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Unable to delete: {e}")
    return {"delete status": "success"}


@app.put('/update_book_details', response_model=schema.Books)
def update_book_details(sl_id: int, update_param: schema.UpdateBook, db: Session = Depends(get_db)):
    details = crud.get_book_by_id(db=db, sl_id=sl_id)
    if not details:
        raise HTTPException(status_code=404, detail=f"No record found to update")

    return crud.update_book_details(db=db, details=update_param, sl_id=sl_id)
