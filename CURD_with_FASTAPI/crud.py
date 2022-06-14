
#  -------------------------------------------------------------------------------
#  Here we are having methods for CRUD operation
#  -------------------------------------------------------------------------------

from sqlalchemy.orm import Session
import model
import schema


def get_movie_by_book_id(db: Session, book_id: str):
    """
    This method will return single book details based on book_id
    :param db: database session object
    :param book_id: book id only
    :return: data row if exist else None
    """
    return db.query(model.Books).filter(model.Books.book_id == book_id).first()


def get_book_by_id(db: Session, sl_id: int):
    """
    This method will return single movie details based on id
    :param db: database session object
    :param sl_id: serial id of record or Primary Key
    :return: data row if exist else None
    """
    return db.query(model.Books).filter(model.Books.id == sl_id).first()


def get_Books(db: Session, skip: int = 0, limit: int = 100):
    """
    This method will return all movie details which are present in database
    :param db: database session object
    :param skip: the number of rows to skip before including them in the result
    :param limit: to specify the maximum number of results to be returned
    :return: all the row from database
    """
    return db.query(model.Books).offset(skip).limit(limit).all()


def add_book_details_to_db(db: Session, Books: schema.BookAdd):
    """
    this method will add a new record to database. and perform the commit and refresh operation to db
    :param db: database session object
    :param movie: Object of class schema.MovieAdd
    :return: a dictionary object of the record which has inserted
    """
    mv_details = model.Books(
        book_id=book.book_id,
        book_name=book.book_name,
        director=book.director,
        geners=book.geners,
        membership_required=book.membership_required,
        cast=book.cast,
        streaming_platform=book.streaming_platform
    )
    db.add(mv_details)
    db.commit()
    db.refresh(mv_details)
    return model.Books(**book.dict())


def update_book_details(db: Session, sl_id: int, details: schema.UpdateBook):
    """
    this method will update the database
    :param db: database session object
    :param sl_id: serial id of record or Primary Key
    :param details: Object of class schema.UpdateMovie
    :return: updated movie record
    """
    db.query(model.Books).filter(model.Books.id == sl_id).update(vars(details))
    db.commit()
    return db.query(model.Books).filter(model.Books.id == sl_id).first()


def delete_book_details_by_id(db: Session, sl_id: int):
    """
    This will delete the record from database based on primary key
    :param db: database session object
    :param sl_id: serial id of record or Primary Key
    :return: None
    """
    try:
        db.query(model.Books).filter(model.Books.id == sl_id).delete()
        db.commit()
    except Exception as e:
        raise Exception(e)
