from sqlalchemy.orm import Session

from models.usuarios import Usuario


def get_user_by_username(db: Session, username: str):
    return db.query(Usuario).filter(Usuario.username == username).first()
